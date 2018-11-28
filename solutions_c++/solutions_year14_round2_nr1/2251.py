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
	int t,i,j,n,n2,k,cnt,min,cc;
	t=ni();
	
	
	FOR(i,t)
	{
		cnt=0;
		cc=0;
		char c;
		char s[110][110];
		char s2[110][110];
		int chk[110][110]={0};
		int actn[2]={0};
		n=ni();
		FOR(j,n)
		{
			s[j][0]='\0';
			s2[j][0]='\0';
			scanf("%s",&s[j]);
			n2=strlen(s[j]);
			FOR(k,n2)
			{
				if(s[j][k]!=s[j][k-1])
				{
					actn[j]++;
					s2[j][actn[j]-1]=s[j][k];
					chk[j][actn[j]-1]=1;
				}
				else
				{
					chk[j][actn[j]-1]++;
				}
			}
			s2[j][actn[j]]='\0';
//			printf("%s\n",s2[j]);
		}
		
		FOR(j,n-1)
		{
			if(actn[j]!=actn[j+1])
			{
				printf("Case #%d: Fegla Won\n",i+1);
				cc=1;
				break;
			}
		}
		if(cc==0){
		
			FOR(k,actn[0])
			{
				min=1000;
				
				c=s2[0][k];
				FOR(j,n)
				{
					if(c==s2[j][k])
					{
						if(min>chk[j][k])
						{
							min=chk[j][k];
						}
					}
					else
					{
						printf("Case #%d: Fegla Won\n",i+1);
						cc=1;
						k=actn[0];
						break;
					}
				}
				FOR(j,n)
				{
					cnt+=chk[j][k]-min;
				}
			}
			if(cc==0)
			printf("Case #%d: %d\n",i+1,cnt);
		}
		
		
	}
	return 0;
}


