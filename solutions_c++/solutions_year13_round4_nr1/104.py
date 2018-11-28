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

#define MOD 1000002013

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N,M;
	int i,j,k,v,x,tot,cur;
	int a,b,p;
	PR E[5000],P[5000],ong[5000];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d: ",t);
			Read(N),Read(M);
			tot=0;
				Fox(i,M)
				{
					Read(a),Read(b),Read(p);
					j=b-a;
					v=(LL)(N+N-j+1)*j/2%MOD;
					tot=(tot+(LL)v*p)%MOD;
					E[i]=mp(a,p);
					E[M+i]=mp(b,-p);
				}
			//printf("%d\n",tot);
			M*=2;
			sort(E,E+M);
			j=0;
				Fox(i,M)
					if ((!i) || (E[i].x!=E[i-1].x))
						P[j++]=E[i];
					else
						P[j-1].y+=E[i].y;
			M=j,j=cur=0;
				Fox(i,M)
					if (P[i].y>0)
						ong[j++]=P[i];
					else
					if (P[i].y<0)
					{
						k=-P[i].y;
							while (k)
							{
								x=min(k,ong[j-1].y);
								a=P[i].x-ong[j-1].x;
								v=(LL)(N+N-a+1)*a/2%MOD;
								cur=(cur+(LL)v*x)%MOD;
								k-=x;
									if (ong[j-1].y==x)
										j--;
									else
										ong[j-1].y-=x;
							}
					}
			//printf("%d\n",cur);
			tot-=cur;
				if (tot<0)
					tot+=MOD;
			printf("%d\n",tot);
		}
	return(0);
}