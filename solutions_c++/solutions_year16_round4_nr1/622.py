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

vi go(int h,int node)
{
	if (h==0)
	{
		vi v(1,node);
		return v;
	}
	if (node==0)
	{
		int node1=0;
		int node2=1;
		vi v1=go(h-1,node1);
		vi v2=go(h-1,node2);
		vi v;
		if (v1>v2) swap(v1,v2);
		v=v1;
		FOR(i,v2.sz) v.pb(v2[i]);
		return v;
	}
	if (node==1)
	{
		int node1=1;
		int node2=2;
		vi v1=go(h-1,node1);
		vi v2=go(h-1,node2);
		vi v;
		if (v1>v2) swap(v1,v2);
		v=v1;
		FOR(i,v2.sz) v.pb(v2[i]);
		return v;
	}
	if (node==2)
	{
		int node1=2;
		int node2=0;
		vi v1=go(h-1,node1);
		vi v2=go(h-1,node2);
		vi v;
		if (v1>v2) swap(v1,v2);
		v=v1;
		FOR(i,v2.sz) v.pb(v2[i]);
		return v;
	}
}


char mem[4];

int main()
{
    int te;
	cin>>te;
	mem[0]='P';
	mem[1]='R';
	mem[2]='S';
	
    FOR(tnr,te)
    {

    	int n,r,p,s;
    	cin>>n>>r>>p>>s;
    	bool jest=0;
    	printf("Case #%d: ",tnr+1);
    	FOR(i,3)
    	{
    		vi v=go(n,i);
    		int z[3]={0};
    		FOR(i,v.sz) z[v[i]]++;
    		if (z[0]==p && z[1]==r && z[2]==s)
    		{
    			jest=1;
    			FOR(i,v.sz) cout<<mem[v[i]];
    			cout<<"\n";
    			break;
    		}
    	}
    	if (!jest) cout<<"IMPOSSIBLE\n";
    	


    }

	return 0;
}


