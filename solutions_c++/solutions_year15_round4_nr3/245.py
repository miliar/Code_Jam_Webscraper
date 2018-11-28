#define DEBUG 1

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=(n)-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x<0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }
string plural(string s) { return(Sz(s) && s[Sz(s)-1]=='x' ? s+"en" : s+"s"); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

//#if DEBUG
#define GETCHAR getchar
/*#else
#define GETCHAR getchar_unlocked
#endif*/

bool Read(int &x)
{
	char c,r=0,n=0;
	x=0;
		for(;;)
		{
			c=GETCHAR();
				if ((c<0) && (!r))
					return(0);
				if ((c=='-') && (!r))
					n=1;
				else
				if ((c>='0') && (c<='9'))
					x=x*10+c-'0',r=1;
				else
				if (r)
					break;
		}
		if (n)
			x=-x;
	return(1);
}

int N,M;
int G[12][12];
int ans[13][13];
int sol[1000000][12][12];

bool check()
{
	int i,j,k,c;
		Fox(i,N)
			Fox(j,M)
			{
				c=0;
					if ((i) && (G[i-1][j]==G[i][j]))
						c++;
					if ((i<N-1) && (G[i+1][j]==G[i][j]))
						c++;
					if (G[i][(j+1)%M]==G[i][j])
						c++;
					if (G[i][(j+M-1)%M]==G[i][j])
						c++;
					if (c!=G[i][j])
						return(0);
			}
		Fox(c,ans[N][M])
			Fox(k,M)
			{
					Fox(i,N)
						Fox(j,M)
							if (G[i][j]!=sol[c][i][(j+k)%M])
								goto Good;
				return(0);
Good:;
			}
		/*Fox(i,N)
		{
			Fox(j,M)
				printf("%d ",G[i][j]);
			printf("\n");
		}
	printf("\n");*/
	return(1);
}

void rec(int i,int j)
{
		if (i==N)
		{
				if (check())
				{
						Fox(i,N)
							Fox(j,M)
								sol[ans[N][M]][i][j]=G[i][j];
					ans[N][M]++;
				}
			return;
		}
	int k;
		Fox1(k,3)
		{
			G[i][j]=k;
				if (j==M-1)
					rec(i+1,0);
				else
					rec(i,j+1);
		}
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("C.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N=0,K;
	int i,j,b,c,ans;
	vector<int> lst[20];
	map<string,int> M;
	string LN,s;
	static char ln[100005];
	static int val[1222];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d: ",t);
				Fox(i,N)
					lst[i].clear();
			Read(N);
			M.clear();
			K=0;
				Fox(i,N)
				{
					cin.getline(ln,100000);
					LN=ln;
					stringstream SS(LN);
						while (SS >> s)
						{
								if (!M.count(s))
									M[s]=K++;
							lst[i].pb(M[s]);
						}
				}
			ans=INF;
				Fox(b,1<<N)
				{
						if (b&1)
							continue;
						if (!(b&2))
							continue;
					Fill(val,0);
						Fox(i,N)
							Fox(j,Sz(lst[i]))
								if (b&(1<<i))
									val[lst[i][j]]|=1;
								else
									val[lst[i][j]]|=2;
					c=0;
						Fox(i,K)
							if (val[i]==3)
								c++;
					Min(ans,c);
				}
			printf("%d\n",ans);
		}
	return(0);
}