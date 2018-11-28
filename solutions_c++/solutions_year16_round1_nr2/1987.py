#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	
	int t;
	cin>>t;
	
	int cnt = 1;
	while(t--)
	{
		int n;
		cin>>n;
		
		vector<int> ans;
		int count[2501];
		
		int i,j;
		for(i=0;i<2501;i++)
			count[i] = 0;
		
		for(i=0;i<2*n-1;i++)
		{
			for(j=0;j<n;j++)
			{
				int r;
				cin>>r;
				count[r]++;
				
			}
		}
		for(i=0;i<2501;i++)
		{
			if(count[i]%2!=0)
				ans.push_back(i);
				
		}	
		sort(ans.begin(), ans.end());
		
		cout<<"Case #"<<cnt<<": ";
		for(i=0;i<ans.size();i++)
			cout<<ans[i]<<" ";
		cout<<endl;
		cnt++;
		
		
	}
	
	
}