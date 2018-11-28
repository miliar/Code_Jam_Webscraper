#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
#include <ctime>
#include <queue>
#include <set>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << (x) << endl;
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int size(const T&c) { return c.size(); }
int rint() { int x; cin>>x; return x; }
LL rLL() { LL x; cin>>x; return x; }
string rstring() { static char buf[100000]; if(scanf("%s",buf)!=1) return ""; return buf; }

struct node
{
	LL s;
	LL e;
	LL p;
};
const LL MOD=1000002013;
struct comp
{
	LL s;
	int t;
	LL p;
	bool operator<(const comp &x)
	{
		if(x.s != s)
			return x.s > s;
		if(x.s == s)
		{
			return x.t > t;
		}
	}
};
vector<node> peopel;
vector<comp> vcomp;
set<LL> sta;
const int NUM=3000;
LL peo[NUM]; 
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test=rint();

	for(int i=0;i<test;i++)
	{
		peopel.clear();
		vcomp.clear();
		//sta.clear();
		LL orgcost=0;
		LL N,M;
		N=rLL();
		M=rLL();
		for(int j=0;j<M;j++)
		{
			node a;
			a.s=rLL();
			a.e=rLL();
			a.p=rLL();
			LL dis=a.e-a.s;
			LL tcost=a.p*(((N+N+1-dis)*dis/2)%MOD);
			tcost%=MOD;
			orgcost+=tcost;
			orgcost%=MOD;
			peopel.push_back(a);
			comp b;
			b.s=a.s;
			b.t=0;
			b.p=a.p;
			vcomp.push_back(b);
			b.s=a.e;
			b.t=1;
			b.p=a.p;
			vcomp.push_back(b);
		}
		memset(peo,0,sizeof(peo));
		sort(vcomp.begin(),vcomp.end());
		int size=vcomp.size();
		LL newcost=0;
		for(int j=0;j<size;j++)
		{
			LL tcost=0;
			comp a=vcomp[j];
			if(a.t==0)
			{
				peo[j]+=a.p;
				continue;
			}
			LL left=a.p;
			for(int k=j-1;k>=0;k--)
			{
				comp b=vcomp[k];
				LL diff=a.s-b.s;
				LL ou=min(left,peo[k]);
				tcost+=ou*(((N+N-diff+1)*diff/2)%MOD);
				tcost%=MOD;
				peo[k]-=ou;
				left-=ou;
				if(left==0) break;
			}
			newcost+=tcost;
			newcost%=MOD;
		}
		LL ans=orgcost+MOD-newcost;
		ans%=MOD;
		cout<<"Case #"<<i+1<<": "<<ans<<endl;

	}

	return 0;
}