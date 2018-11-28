#include<bits/stdc++.h>
using namespace std;

#define fre freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
#define ll long long
#define abs(x) ((x)>0?(x):-(x))
#define mod 1000000007
#define scand(x) scanf("%d",&x);
#define scanlld(x) scanf("%I64d",&x);
#define scans(x) scanf("%s",x);
#define printd(x) printf("%d",x);
#define printlld(x) printf("%I64d",x);
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define inf (1<<30)
#define forup(i,a,b) for(int i=a;i<b;i++)
#define pii pair<int,int>
#define boost ios_base::sync_with_stdio(0)
#define MAXN 100003
int vis[12];
int main()
{
	boost;
	fre;
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		memset(vis,0,sizeof(vis));
		long long n;
		cin>>n;
		cout<<"Case #"<<tt<<": ";
		if(n==0){cout<<"INSOMNIA"<<endl;continue;}
		long long i=1,cnt=0;
		while(cnt!=10)
		{
			long long val=i*n;
			while(val>0)
			{
				if(vis[val%10]!=1)vis[val%10]=1,cnt++;
				val/=10;
			}
			i++;
		}
		cout<<n*(i-1)<<endl;
	}
	return 0;
}