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

char let[3]={'R','P','S'};

char Win(char a,char b)
{
		if (a>b)
			swap(a,b);
		if ((a=='P') && (b=='R'))
			return('P');
		if ((a=='P') && (b=='S'))
			return('S');
	return('R');
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N,R,P,S;
	int i,j,a,b,r,p,s;
	string ans;
	string s1,s2;
	static string tr[13][3];
	tr[0][0]="R";
	tr[0][1]="P";
	tr[0][2]="S";
		Fox1(i,12)
			Fox(j,3)
				Fox(a,3)
					Fox(b,a)
						if (Win(let[a],let[b])==let[j])
						{
							s1=tr[i-1][a];
							s2=tr[i-1][b];
								if (s1>s2)
									swap(s1,s2);
							tr[i][j]=s1+s2;
						}
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d: ",t);
			Read(N),Read(R),Read(P),Read(S);
			ans="Z";
				Fox(i,3)
				{
					r=R,p=P,s=S;
					s1=tr[N][i];
						Fox(j,Sz(s1))
							if (s1[j]=='R')
								r--;
							else
							if (s1[j]=='P')
								p--;
							else
								s--;
						if ((!r) && (!p) && (!s))
							Min(ans,s1);
				}
				if (ans=="Z")
					ans="IMPOSSIBLE";
			cout << ans << endl;
		}
	return(0);
}