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
const double EPS = 1e-9;
const LD PI = acos(-1.0);

#define MOD 1000000007

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

int N;
int BLT[1001];

void update(int i,int v)
{
	for (;i<=N;i+=(i&-i))
		BLT[i]+=v;
}

int query(int i)
{
	int v=0;
		for (;i>0;i-=(i&-i))
			v+=BLT[i];
	return(v);
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int i,j,d,ans;
	int V[1000],res1,res2,C[1000];
	int V2[1000],ind[1001];
	int dyn[1000][1000];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d: ",t);
			Read(N);
				Fox(i,N)
					Read(V[i]),C[i]=V[i];
			sort(C,C+N);
				Fox(i,N)
					V[i]=lower_bound(C,C+N,V[i])-C+1;
			int ans2=INF;
				Fox(i,N)
					ind[V[i]]=i;
			/*memcpy(V2,V,sizeof(V));
			int out[1000];
			sort(V2,V2+N);
				do
				{
					bool s=0;
						Fox(i,N-1)
							if (V2[i]<V2[i+1])
							{
								if (s)
									goto Bad;
							}
							else
								s=1;
					int c=0,j;
						Fox(i,N)
							Fox(j,i)
								if (ind[V2[i]]<ind[V2[j]])
									c++;
						if (c<=ans2)
						{
							ans2=c;
							memcpy(out,V2,sizeof(out));
						}
Bad:;
				}
				while (next_permutation(V2,V2+N));*/
			Fill(dyn,60);
			dyn[0][0]=0;
			Fill(BLT,0);
				Fox1(i,N)
					update(i,1);
				Fox1(d,N-1)
				{
					int k=ind[d];
						Fox(i,d)
						{
							j=d-i-1;
							int c1=query(k);
							int c2=query(N)-c1-1;
							Min(dyn[i+1][j],dyn[i][j]+c1);
							Min(dyn[i][j+1],dyn[i][j]+c2);
						}
					update(k+1,-1);
				}
			ans=INF;
				Fox(i,N)
					Min(ans,dyn[i][N-i-1]);
			printf("%d\n",ans);
				/*if (ans!=ans2)
				{
						Fox(i,N)
							printf("%d ",V[i]);
					printf("\n");
						Fox(i,N)
							printf("%d ",out[i]);
					printf("\n");
					printf("%d instead of %d\n",ans,ans2);
				}*/
		}
	return(0);
}