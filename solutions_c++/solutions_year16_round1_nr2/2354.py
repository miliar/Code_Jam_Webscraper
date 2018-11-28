#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

int main()
{
	int t,p=1;cin>>t;
	while(t--)
	{ 
	    int n,x,cntx[2510],ans[55],ind=0;
	    cin>>n;
	    memset(cntx,0,sizeof(cntx));
		for(int i=0;i<2*n-1;i++)
		{
			for(int j=0;j<n;j++)
			cin>>x,cntx[x]++;
		}
		for(int i=0;i<2510;i++)
		{
			if(cntx[i]&1)
			ans[ind++]=i;
		}
		cout<<"Case #"<<p<<": ";
		for(int i=0;i<n;i++)
		cout<<ans[i]<<" ";
		cout<<"\n";
		p++;
	}
}
