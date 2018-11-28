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
#define FoxR(i,n) for (i=n-1; i>=0; i--)
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
 
#if DEBUG
#define GETCHAR getchar
#else
#define GETCHAR getchar_unlocked
#endif
 
void Read(int &x)
{
	char c,r=0,n=0;
	x=0;
		for(;;)
		{
			c=GETCHAR();
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
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("c.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N;
	int i,j,v;
	int A[2005],B[2005],X[2005];
	int up[2005],down[2005],up2[2005],down2[2005];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d:",t);
			Read(N);
				Fox(i,N)
					Read(A[i]);
				Fox(i,N)
					Read(B[i]);
			Fill(up,0);
			Fill(down,0);
				Fox1(v,N)
				{
					Fox(i,N)
						if ((A[i]==up[i]+1) && (B[i]==down[i]+1))
						{
							memcpy(up2,up,sizeof(int)*N);
							memcpy(down2,down,sizeof(int)*N);
								FoxI(j,i+1,N-1)
									if (A[j]>=0)
									{
										up2[j]=max(up[j],A[i]);
											if (up2[j]+1>A[j])
												goto Bad;
									}
								Fox(j,i)
									if (A[j]>=0)
									{
										down2[j]=max(down[j],B[i]);
											if (down2[j]+1>B[j])
												goto Bad;
									}
							memcpy(up,up2,sizeof(int)*N);
							memcpy(down,down2,sizeof(int)*N);
							X[i]=v;
							A[i]=B[i]=-1;
							break;
Bad:;
						}
					if (i==N)
						printf("BAD\n");
				}
				Fox(i,N)
					printf(" %d",X[i]);
			printf("\n");
		}
	return(0);
}