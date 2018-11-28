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
#define LD double
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

LD dist;
int X[1000],Y[1000],Z[1000],Vx[1000],Vy[1000],Vz[1000];
LD A[1000][1000],B[1000][1000];
LD CCC[1000][1000];

LD Dist(LD x,LD y,LD z)
{
	return(sqrt(Sqr(x)+Sqr(y)+Sqr(z)));
}


void FindM(int i,int j)
{
	LD r1,r2,m,m1,m2,v1,v2,cc;
	LD x1,y1,z1,x2,y2,z2;
		if ((Vx[i]==Vx[j]) && (Vy[i]==Vy[j]) && (Vz[i]==Vz[j]))
			return;
	//find min
	r1=0,r2=1e5;
		while (r2>r1+EPS)
		{
			m1=(r1+r1+r2)/3;
			m2=(r1+r2+r2)/3;
			//1
			x1=X[i]+Vx[i]*m1;
			y1=Y[i]+Vy[i]*m1;
			z1=Z[i]+Vz[i]*m1;
			x2=X[j]+Vx[j]*m1;
			y2=Y[j]+Vy[j]*m1;
			z2=Z[j]+Vz[j]*m1;
			v1=Dist(x2-x1,y2-y1,z2-z1);
			//2
			x1=X[i]+Vx[i]*m2;
			y1=Y[i]+Vy[i]*m2;
			z1=Z[i]+Vz[i]*m2;
			x2=X[j]+Vx[j]*m2;
			y2=Y[j]+Vy[j]*m2;
			z2=Z[j]+Vz[j]*m2;
			v2=Dist(x2-x1,y2-y1,z2-z1);
			//go
				if (v1<v2)
					r2=m2;
				else
					r1=m1;
		}
	CCC[i][j]=CCC[j][i]=r1;
}

void Comp(int i,int j)
{
	LD r1,r2,m,m1,m2,v1,v2,cc;
	LD x1,y1,z1,x2,y2,z2;
		if ((Vx[i]==Vx[j]) && (Vy[i]==Vy[j]) && (Vz[i]==Vz[j]))
		{
				if (Dist(X[i]-X[j],Y[i]-Y[j],Z[i]-Z[j])>dist)
					goto Nope;
			A[i][j]=A[j][i]=0;
			B[i][j]=B[j][i]=1e5;
			return;
		}
	//bad?
	cc=CCC[i][j];
	m1=cc;
	x1=X[i]+Vx[i]*m1;
			y1=Y[i]+Vy[i]*m1;
			z1=Z[i]+Vz[i]*m1;
			x2=X[j]+Vx[j]*m1;
			y2=Y[j]+Vy[j]*m1;
			z2=Z[j]+Vz[j]*m1;
			v1=Dist(x2-x1,y2-y1,z2-z1);
		if (v1>dist)
		{
Nope:;
			A[i][j]=A[j][i]=B[i][j]=B[j][i]=-1;
			return;
		}
	//find start
	r1=0,r2=cc;
		while (r2>r1+EPS)
		{
			m=(r1+r2)/2;
			m1=m;
			x1=X[i]+Vx[i]*m1;
			y1=Y[i]+Vy[i]*m1;
			z1=Z[i]+Vz[i]*m1;
			x2=X[j]+Vx[j]*m1;
			y2=Y[j]+Vy[j]*m1;
			z2=Z[j]+Vz[j]*m1;
			v1=Dist(x2-x1,y2-y1,z2-z1);
				if (v1>dist)
					r1=m;
				else
					r2=m;
		}
	A[i][j]=A[j][i]=r1;
	//find end
	r1=cc,r2=1e5;
		while (r2>r1+EPS)
		{
			m=(r1+r2)/2;
			m1=m;
			x1=X[i]+Vx[i]*m1;
			y1=Y[i]+Vy[i]*m1;
			z1=Z[i]+Vz[i]*m1;
			x2=X[j]+Vx[j]*m1;
			y2=Y[j]+Vy[j]*m1;
			z2=Z[j]+Vz[j]*m1;
			v1=Dist(x2-x1,y2-y1,z2-z1);
				if (v1<dist)
					r1=m;
				else
					r2=m;
		}
	B[i][j]=B[j][i]=r1;
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N,S;
	int i,j;
	LD v1,v2;
	LD r1,r2,m;
	LD V1[1000],V2[1000];
	priority_queue<pair<pair<LD,LD>,int> > Q;
	Read(T);
	//T=20;
		Fox1(t,T)
		{
			Read(N),Read(S);
			//N=1000,S=10;
				Fox(i,N)
					Read(X[i]),Read(Y[i]),Read(Z[i]),Read(Vx[i]),Read(Vy[i]),Read(Vz[i]);
				/*{
					X[i]=rand()%100;
					Y[i]=rand()%100;
					Z[i]=rand()%100;
					Vx[i]=rand()%20-10;
					Vy[i]=rand()%20-10;
					Vz[i]=rand()%20-10;
				}*/
				Fox(i,N)
					Fox(j,i)
						FindM(i,j);
			r1=0,r2=1e5;
				while (r2>r1+1e-6)
				{
					m=(r1+r2)/2;
					dist=m;
						Fox(i,N)
							Fox(j,i)
								Comp(i,j);
						while (!Q.empty())
							Q.pop();
						Fox(i,N)
							V1[i]=V2[i]=-1;
					V1[0]=V2[0]=0;
					Q.push(mp(mp(0,0),0));
						while (!Q.empty())
						{
							v1=-Q.top().x.x;
							v2=-Q.top().x.y;
							i=Q.top().y;
							Q.pop();
								if (fabs(v1-V1[i])>EPS)
									continue;
								if (fabs(v2-V2[i])>EPS)
									continue;
							//printf("%d %lf %lf\n",i,V1[i],V2[i]);
								if (i==1)
									goto Good;
								Fox(j,N)
									if (j!=i)
									{
											if (A[i][j]<-0.5)
												continue;
											if ((V2[i]+S<A[i][j]) || (V1[i]>B[i][j]))
												continue;
										v1=max(V1[i],A[i][j]);
										v2=B[i][j];
										Min(v2,(LD)1e5);
											if (V1[j]>-0.5)
											{
												Min(v1,V1[j]);
												Max(v2,V2[j]);
											}
											if ((v1<V1[j]-EPS) || (v2>V2[j]+EPS))
											{
												V1[j]=v1;
												V2[j]=v2;
												Q.push(mp(mp(-v1,-v2),j));
											}
									}
						}
					r1=m;
					continue;
Good:;
					r2=m;
				}
			printf("Case #%d: %.9lf\n",t,r1);
		}
	return(0);
}