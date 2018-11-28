#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
#define trvr(y,x) for(typeof(x.rbegin())y=x.rbegin();y!=x.rend();y++)
#define pb(f) push_back(f)
#define pi_ printf("\n")
#define pi(a) printf("%d\n",a)
#define pil(a) printf("%lld\n",a)
#define sc(a) scanf("%d",&a)
#define ll long long
#define scl(a) scanf("%lld",&a)
#define scs(a) scanf("%s",a)
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007
#define inf 1000000009
#define maxn 100009
using namespace std;
//#include<windows.h>
FILE *fin = freopen("1.in","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
using namespace std;
typedef pair<int,int> pii;
typedef vector<int > vi;
typedef vector< pii > vpii;

int main()
{
	int t,i,j,k,cas=0;
	sc(t);while(t--)
	{
		cas++;	printf("Case #%d: ",cas);
		string s,ans;
		cin>>s;
		ans.pb(s[0]);char last=s[0];
		rep(i,1,s.length())
		{
			if(s[i]>=last)
			{
				string t;t.pb(s[i]);
				ans=t+ans;
				last=s[i];
			}
			else {
				string t;t.pb(s[i]);
				ans=ans+t;
			}
			
		}
		cout<<ans<<endl;
		
	}
}
