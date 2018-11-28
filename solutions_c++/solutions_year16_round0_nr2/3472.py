		/*masterwayne*/
#include<bits/stdc++.h>
using namespace std;
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf(x) printf("%d",x)
#define pf2(x,y) printf("%d %d",x,y)
#define pf3(x,y,z) printf("%d %d %d",x,y,z)
#define fr(i,x,n) for(int i=x;i<n;i++)
#define fre(i,x,n) for(int i=x;i<=n;i++)
#define fb(i,x,n) for(int i=n-1;i>=x;i--)
#define fbe(i,x,n) for(int i=n;i>=x;i--)
#define pfn() printf("\n")
#define pfs() printf(" ")
#define pb push_back
int main()
{
	//freopen("inp11.in","r",stdin);
	//freopen("out1.txt","w",stdout);
	int t;
	sc(t);
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		int l=s.length();
		long long int ans=0;
		for(int j=1;j<l;j++)
		{
			if(s[j]!=s[j-1])
			{
				if(s[j]=='-')
					ans+=2;
			}
		}
		if(s[0]=='-')
			ans+=1;
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}