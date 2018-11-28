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
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define FORD(i,x,v)for(int i=x;i>=v;i--)
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


const long double eps = 1e-14;

typedef long double LD;


LD R[1111],C[1111];

int main()
{
	int te;
	cin>>te;
	
	
    FOR(tnr,te)
    {
    	int n;
    	LD V,X;
    	cin>>n>>V>>X;
    	FOR(i,n)cin>>R[i]>>C[i];
    	LD mnt=1e8,mxt=-1e8;
    	FOR(i,n)
    	{
    		REMIN(mnt,C[i]);
    		REMAX(mxt,C[i]);
    	}
    	
    	if (mnt>X+eps || mxt<X-eps)
    	{
    		printf("Case #%d: ",tnr+1);
    		cout<<"IMPOSSIBLE\n";
    		continue;
    	}
    	LD lo = 0.0, hi=1e18,mid;
    	FOR(sdf,2000)
    	{
    		mid=(hi+lo)/2;
    		vector<pair<LD,LD> > v;
    		FOR(i,n) v.pb(mp(C[i],R[i]));
    		sort(ALL(v));
    		FOR(i,n) {C[i]=v[i].fi;R[i]=v[i].se;}
    		LD mx=0,mn=0;
    		LD sx=0,sn=0;
    		FOR(i,n)
    		{
    			LD g=(V-sn)/R[i];
    			g=min(g,mid);
    			mn+=R[i]*g*C[i];
    			sn+=g*R[i];
    		}
    		reverse(ALL(v));
    		FOR(i,n) {C[i]=v[i].fi;R[i]=v[i].se;}
    		FOR(i,n)
    		{
    			LD g=(V-sx)/R[i];
    			g=min(g,mid);
    			mx+=R[i]*g*C[i];
    			sx+=g*R[i];
    		}
    		if (mn-eps<V*X && V*X<mx+eps) hi=mid;
    		else lo=mid;
    	}
    	printf("Case #%d: ",tnr+1);
    	cout<<fixed<<setprecision(10);
    	cout<<hi<<endl;
    	
    	
    }

	return 0;
}
