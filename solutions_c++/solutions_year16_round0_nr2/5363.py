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
int ans=0;
char a[105];
void rec(int st,int en)
{
	if(en<st) return;
	while(en>=st)
	{
		if(a[en]=='+')
		en--;
		else break;
	}
	if(en<st) return ;
	int i,j;
	if(a[st]=='-')
	{
		//pi(1);
		ans++;
		i=st,j=en;
		while(i<=j)
		{
			swap(a[i],a[j]);
			i++;j--;
		}
		i=st,j=en;
		while(i<=en)
		{
			if(a[i]=='+') a[i]='-';
			else a[i]='+';
			i++;
		}
		rec(st,en);
	//	pi(12);
	}
	else
	{
	//	pi(2);
		ans++;
		i=st;
		while(a[i]=='+'&&i<=en)
		i++;
		j=i-1;
		i=st;
		while(i<=j) {
		a[i]='-';i++;}
		rec(st,en);
	}
	
}
int main()
{
	int cas=0,t;
	sc(t);while(t--)
	{
		cas++;int n;
		scs(a+1);
		printf("Case #%d: ",cas);ans=0;
		n=strlen(a+1);
		rec(1,n);
		pi(ans);
	}
}
