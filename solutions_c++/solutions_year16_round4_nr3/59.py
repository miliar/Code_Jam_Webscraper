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
const LD EPS = 1e-12;
const LD PI = acos(-1.0);

#if DEBUG
#define GETCHAR getchar
#else
#define GETCHAR getchar_unlocked
#endif

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

int ind[50][50];
char G[50][50];

int Go(int y,int x,int dy,int dx)
{
		if (ind[y][x]>=0)
			return(ind[y][x]);
	swap(dy,dx);
		if (G[y][x]=='/')
			dy=-dy,dx=-dx;
	return(Go(y+dy,x+dx,dy,dx));
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int R,C,N,M,B;
	int i,j,a,b,bb,dy,dx;
	int V[50],tmp[50],inv[50];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d:\n",t);
			Read(R),Read(C);
			N=2*(R+C);
			M=R*C;
			B=1<<M;
				Fox(i,N)
					Read(tmp[i]),tmp[i]--,inv[tmp[i]]=i;
				Fox(i,N)
					V[i]=inv[i]/2;
			j=0;
			Fill(ind,-1);
				Fox(i,C)
					ind[0][i+1]=V[j++];
				Fox(i,R)
					ind[i+1][C+1]=V[j++];
				FoxR(i,C)
					ind[R+1][i+1]=V[j++];
				FoxR(i,R)
					ind[i+1][0]=V[j++];
				Fox(bb,B)
				{
						Fox(i,M)
						{
							a=i/C+1;
							b=i%C+1;
								if (bb&(1<<i))
									G[a][b]='/';
								else
									G[a][b]='\\';
						}
						Fox(i,R+2)
							Fox(j,C+2)
								if (ind[i][j]>=0)
								{
									dy=dx=0;
										if (!i)
											dy=1;
										if (i>R)
											dy=-1;
										if (!j)
											dx=1;
										if (j>C)
											dx=-1;
										if (Go(i+dy,j+dx,dy,dx)!=ind[i][j])
											goto Bad;
								}
						Fox1(i,R)
						{
								Fox1(j,C)
									printf("%c",G[i][j]);
							printf("\n");
						}
					goto Done;
Bad:;
				}
			printf("IMPOSSIBLE\n");
Done:;
		}
	return(0);
}