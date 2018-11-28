#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstring>
#include <complex>
#include <ctime>
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define REPD(i,x,v)for(int i=x;i>=v;i--)
#define FOR(i,v)for(int i=0;i<v;i++)
#define FORE(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REMIN(x,y) (x)=min((x),(y))
#define REMAX(x,y) (x)=max((x),(y))
#define pb push_back
#define sz size()
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define IN(x,y) ((y).find((x))!=(y).end())
#define un(v) v.erase(unique(ALL(v)),v.end())
#define LOLDBG
#ifdef LOLDBG
#define DBG(vari) cerr<<#vari<<" = "<<vari<<endl;
#define DBG2(v1,v2) cerr<<(v1)<<" - "<<(v2)<<endl;
#else
#define DBG(vari)
#define DBG2(v1,v2)
#endif
#define CZ(x) scanf("%d",&(x));
#define CZ2(x,y) scanf("%d%d",&(x),&(y));
#define CZ3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z));
#define ALL(x) (x).begin(),(x).end()
#define tests int dsdsf;cin>>dsdsf;while(dsdsf--)
#define testss int dsdsf;CZ(dsdsf);while(dsdsf--)
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }
typedef vector<double> vd;

vd prob(double p)
{
	vd v(2);
	v[0]=p;
	v[1]=1-p;
	return v;
}


vd zero()
{
	return vd(1,1.0);
}

vd conv(vd v1,vd v2)
{
	int k1=v1.sz;
	int k2=v2.sz;
	vd v(k1+k2-1,0.0);
	FOR(i,k1)FOR(j,k2) v[i+j]+=v1[i]*v2[j];
	return v;
}

long double p[1111];
int n,k;
vd dp[222][222];//dp[n][ky][kn];

double brute()
{
	double mx=0;
	FOR(i,(1<<n))
	{
		if (__builtin_popcount(i)!=k) continue;
		vd v=zero();
		FOR(j,n) if ((1<<j)&i) v=conv(v,dp[j][j+1]);
		REMAX(mx,v[k/2]);
	}
	return mx;
}
vi best;
double bestpro;

bool local()
{
	vd cb=zero();
	FOR(i,best.sz) cb=conv(cb,prob(p[best[i]]));
	set<int> allb(ALL(best));
	FOR(i,k)
	{
		vd cb2=zero();
		FOR(j,k) if (i!=j) cb2=conv(cb2,prob(p[best[j]]));
		FOR(j,n)
		{
			if (!IN(j,allb))
			{
				vd cb3=conv(cb2,prob(p[j]));
				if (cb3[k/2]>bestpro)
				{
					best[i]=j;
					bestpro=cb3[k/2];
					return 1;
				}
			}
		}
	}
	return 0;
	
}

int main()
{
    int te;
	cin>>te;
	
	
    FOR(tnr,te)
    {
		cin>>n>>k;
		FOR(i,n) cin>>p[i];
		sort(p,p+n);
		FOR(i,n)
		{
			dp[i][i]=zero();
			dp[i][i+1]=prob(p[i]);
		}
		FOR(i,n+1)FOR(j,i)
		{
			if (i-j<=1) continue;
			else dp[j][i]=conv(dp[j][i-1],dp[i-1][i]);
		}
		double mx=-1;
		
		FOR(d,n+1)FOR(c,d+1)FOR(b,c+1)FOR(a,b+1)
		{
			if (a+(c-b)+(n-d)!=k) continue;
			vd v=conv(conv(dp[0][a],dp[b][c]),dp[d][n]);
			if (v[k/2]>mx)
			{
				REMAX(mx,v[k/2]);
				best.clear();
				FOR(i,n) if (i<a || (i>=b && i<c) || (i>=d)) best.pb(i);
			}
		}
		bestpro=mx;
		while(1)
		{
			if (!local()) break;
		}
		
    	
    	printf("Case #%d: ",tnr+1);
    	cout<<fixed<<setprecision(9)<<bestpro<<"\n";
    	//cout<<fixed<<setprecision(9)<<brute()<<" "<<mx<<"\n";


    }

	return 0;
}


