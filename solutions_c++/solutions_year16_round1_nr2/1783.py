#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>

using namespace std;

int main()
{
	int cases=0;
	cin >> cases;
	for(int k=1;k<=cases;k++)
	{
		int n,m;
		cin >>n;

		map<int,int> M;
		vector< vector<int> > inp(2*n-1,vector<int>(n,0));
		for(int i=0;i<2*n-1;i++)
		{
			for(int j=0;j<n;j++) 
			{
				cin >> inp[i][j];
				if(M.find(inp[i][j])==M.end()) M[inp[i][j]]=0;
				M[inp[i][j]] = M[inp[i][j]]+1;
			}
		}
		vector<int> ans;
		for(map<int,int>::iterator it=M.begin();it!=M.end();it++)
		{
			if(it->second%2) ans.push_back(it->first);
		}
		sort(ans.begin(),ans.end());
		cout << "Case #" << k <<": ";
		for(int i=0;i<ans.size();i++) cout << ans[i] << " ";
		cout << endl;
	}
	return 0;
}
