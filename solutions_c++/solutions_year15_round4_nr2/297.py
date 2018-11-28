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

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("B.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N;
	LD V,X;
	int i;
	LD r,v1,v2;
	LD R[5],C[5];
	Read(T);
		Fox1(t,T)
		{
			Read(N);
			cin >> V >> X;
				Fox(i,N)
					cin >> R[i] >> C[i];
				if (N>2)
					continue;
			printf("Case #%d: ",t);
				if (N==1)
				{
One:;
						if (fabs(C[0]-X)>EPS)
							goto Imp;
					printf("%.9Lf\n",V/R[0]);
					continue;
				}
				if (fabs(C[0]-C[1])<EPS)
				{
					R[0]+=R[1];
					goto One;
				}
				if (C[0]>C[1])
				{
					swap(R[0],R[1]);
					swap(C[0],C[1]);
				}
				if (X<C[0]-EPS)
					goto Imp;
				if (X>C[1]+EPS)
					goto Imp;
			r=(X-C[0])/(C[1]-C[0]);
			v1=V*(1-r);
			v2=V*r;
			LD tmp=(C[0]*v1+C[1]*v2)/V;
				if (fabs(tmp-X)>EPS)
					printf("WTF\n");
			printf("%.9Lf\n",max(v1/R[0],v2/R[1]));
			continue;
Imp:;
			printf("IMPOSSIBLE\n");
		}
	return(0);
}