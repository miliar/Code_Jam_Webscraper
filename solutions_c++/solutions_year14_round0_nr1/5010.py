# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <numeric>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <deque>
# include <ctime>
# include <stack>
# include <queue>
# include <cctype>
# include <bitset>
# include <complex>

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,PII> TPI;
typedef vector<string> VS;

#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Pf(n)	    printf("%f\n",n)
#define Ss(n)       scanf("%s",&n)
#define Ps(n)	    printf("%s\n",n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define FOR(i,n) REP(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define bitcount(x) __builtin_popcount(x)
#define pb push_back
#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define EPS (double)(1e-9)
#define INF 1000000000
#define MOD 1000000007
#define PI (double)(3.141592653589793)

//int flag[>>5]={0};
#define ifc(x) (flag[x>>5]&(1<<(x&31)))  //(n)%32 = (n)&31 ; 1<<((x)&31))= pushing 1 to specific bit n then perform and operation.
#define isc(x) (flag[x>>5]|=(1<<(x&31))) //x|=1  => x=x|1;

#ifdef _WIN32
// no getchar_unlocked on Windows so just call getchar
inline int getchar_unlocked() { return getchar(); }
#endif

inline int ni()
{
	register int r=0,c;
	for(c=getchar_unlocked();c<=32;c=getchar_unlocked());
	if(c=='-')
		return -ni();
	for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar_unlocked());
	return r;
}
int main()
{
	int t,a,b,m[5][5],ans[20],chk,n,i,j,k;
	t=ni();
	FOR(k,t)
	{
		CLR(ans);
		chk=0;
		scanf("%d",&a);
		FOR(i,4)
		{
			FOR(j,4)
			{
				scanf("%d",&m[i][j]);
			}
		}
		FOR(i,4)
		{
			ans[m[a-1][i]]++;
		}
		scanf("%d",&b);
		FOR(i,4)
		{
			FOR(j,4)
			{
				scanf("%d",&m[i][j]);
			}
		}
		FOR(i,4)
		{
			ans[m[b-1][i]]++;
		}
		FOR(i,17)
		{
			if(ans[i]==2)
			{
				chk++;
				n=i;
			}
//			printf("%d\t",ans[i]);
		}
		if(chk==1)
		{
			printf("Case #%d: %d\n",k+1,n);
		}
		else if(chk>=2)
		{
			printf("Case #%d: Bad magician!\n",k+1);	
		}
		else
			printf("Case #%d: Volunteer cheated!\n",k+1);
	}
	return 0;
}


