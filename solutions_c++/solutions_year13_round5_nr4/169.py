#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
double dp[1111111];
bool v[1111111];
char s[33];
int n;
double getdp(int x)
{
	if (v[x])return dp[x];
	if ((x==(1<<n)-1))return dp[x]=0;
	//printf("%d\n",x);
	int i,j;
	double aa=0;
	for (i=0;i<n;i++)
	{
		int ps=-1,sum=0;
		for (j=i;j<n;j++)
		{
			if ((x&(1<<(n-j-1)))==0)
			{
				ps=j;break;
			}
		}
	/*	
		if (x==6&&i==0)
		{
			printf("%d\n",ps);
			system("pause");
		}
		*/
		if (ps==-1)
		{
			for (j=0;j<i;j++)
			{
				if ((x&(1<<(n-j-1)))==0)
				{
					ps=j;break;
				}
			}
			sum=n-((n-i)+ps);
		}
		else 
		{
			sum=n-(ps-i);
		}
		//printf("%d %d %d %d %d\n",x,n,i,ps,sum);
		aa+=(1.0/n)*(sum+getdp(x|(1<<(n-1-ps))));
	}
	v[x]=1;
	return dp[x]=aa;
}
		
		
int main()
{
	freopen("C://ddd123.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%s",s);
		n=strlen(s);
		int st=0;
		for (i=0;i<n;i++)
		{
			if (s[i]=='X')
			{
				st|=1<<(n-1-i);
			}
		}
		for (i=0;i<(1<<n)+100;i++)dp[i]=-1;
		clr(v);
		printf("Case #%d: %.15lf\n",++cc,getdp(st));
	}
	return 0;
}
				
		
	
