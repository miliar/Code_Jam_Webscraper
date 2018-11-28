#include <bits/stdc++.h>
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define ll long long
#define ull unsigned ll
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);//redirects standard input
    freopen("output.txt","w",stdout);//redirects standard output
	int t,j,sm,i;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		string s;
		cin>>sm>>s;
		int ans=0,l=s.size(),b=0;
		for(i=0;i<l;i++)
		{
			b+=s[i]-'0';
			if(b<i+1)
			{
				ans+=(i+1-b);
				b=i+1;
			}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;	
	}
	return 0;
}
    