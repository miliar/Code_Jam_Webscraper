#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(auto y=x.begin();y!=x.end();y++)
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
bool check (string s)
{
//	cout<<"P"<<endl;
	string t;
	if(s.length()==1) return 1;
	for(int i=0;i<s.length();i+=2)
	{
		if((s[i]=='R'&&s[i+1]=='S')||(s[i]=='S'&&s[i+1]=='R'))
		{
			t.pb('R');
		}
		else if((s[i]=='R'&&s[i+1]=='P')||(s[i]=='P'&&s[i+1]=='R'))
		t.pb('P');
		else if((s[i]=='S'&&s[i+1]=='P')||(s[i]=='P'&&s[i+1]=='S'))
		t.pb('S');
		else
		{
			return 0;
		}
	}
	if(check(t)) return 1;
	return 0;
}
int main()
{
	int t,i,j,k,cas=0;
	sc(t);while(t--)
	{
		cas++;	printf("Case #%d: ",cas);
		int n;cin>>n;int i,j,k,l;
		int r,p,s;
		cin>>r>>p>>s;
		int temp=1;
		rep(i,1,n+1)
		{
			temp*=2;
		}
		n=temp;
		string v;
		rep(i,1,p+1)
		{
			v.pb('P');
		}rep(i,1,r+1)
		{
			v.pb('R');
		}rep(i,1,s+1)
		{
			v.pb('S');
		}int f=0;
		do
		{
			if(check(v))
			{
				f=1;
				break;
			}
		}while(next_permutation(v.begin(),v.end()));
		if(f)
		cout<<v<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
		
	}
}
