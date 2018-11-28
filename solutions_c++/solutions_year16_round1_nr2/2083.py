//By SCJ
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int b[2505];
int main()
{
ios::sync_with_stdio(0);
cin.tie(0);
	int T;cin>>T;
	for(int no=1;no<=T;++no)
	{
		int n;cin>>n;
		for(int i=0;i<2505;++i) b[i]=0;
		for(int i=0;i<2*n-1;++i)
		{
			for(int j=0;j<n;++j)
			{
				int x;cin>>x;
				b[x]++;
			}
		}
		vector<int> ans;
		for(int i=0;i<2505;++i)
		{
			if(b[i]&1) ans.push_back(i);
		}
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<no<<": ";
		for(int i=0;i<n;++i)
		{
			if(i!=0) cout<<' ';
			cout<<ans[i];
		}

		cout<<endl;
	}
}
