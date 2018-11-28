#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <cstdlib>
#include <cctype>
#include <bitset>
#include <string>
#include <map>
#include <cassert>
#include <set>

#ifdef PEYEK 
	#define debugln {printf("----OK----\n");}
	#define debug(...) {printf(__VA_ARGS__);}
	#define debugs(...) {printf(":::::--->> ");printf(__VA_ARGS__);}
	#define TIME() printf("%.3lf\n",clock()/(double)CLOCKS_PER_SEC)
#else
	#define debugln {}
	#define debug(...) {}
	#define debugs(...) {}
	#define TIME() {}
#endif

#ifdef __WIN32__
	char getchar_unlocked() {return getchar();}
#endif

#define FOR(_i,_n,_m) for(int (_i)=(_n),_t=(_m);_i<(_t);++(_i))
#define FORN(_i,_n,_m) for(int (_i)=(_n),_t=(_m);_i<=(_t);++(_i))
#define FORD(_i,_n,_m) for(int (_i)=(_n),_t=(_m);_i>=(_t);--(_i))
#define FORLL(_i,_n,_m) for(long long (_i)=(_n),_t=(_m);_i<(_t);++(_i))
#define FORNLL(_i,_n,_m) for(long long (_i)=(_n),_t=(_m);(_i)<=(_t);++(_i))
#define FORDLL(_i,_n,_m) for(long long (_i)=(_n),_t=(_m);(_i)>=(_t);--(_i))
#define FOREACH(_i,_a) for (__typeof(_a.begin()) _i=_a.begin();_i!=_a.end();++_i)
#define RESET(_a,_value) memset(_a,_value,sizeof(_a))
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define ff first
#define ss second
#define mp make_pair
#define SIZE(_a) (int)_a.size()
#define VSORT(_a) sort(_a.begin(),_a.end())
#define SSORT(_a,_val) sort(_a,_a+(_val))
#define ALL(_a) _a.begin(),_a.end()
 
using namespace std;
 
const int dr[]={ 1, 0,-1, 0, 1, 1,-1,-1};
const int dc[]={ 0, 1, 0,-1, 1,-1,-1, 1};
const double eps=1e-9;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef vector<pll> vpll;
typedef vector<ll> vll;
typedef pair<double,double> pdd;
typedef vector<pdd> vpdd;
const int INF=0x7FFFFFFF;
const ll INFLL=0x7FFFFFFFFFFFFFFFLL;
const double pi=acos(-1);

template <class T> T take(queue<T> &O) {T tmp=O.front();O.pop();return tmp;}
template <class T> T take(stack<T> &O) {T tmp=O.top();O.pop();return tmp;}
template <class T> T take(priority_queue<T> &O) {T tmp=O.top();O.pop();return tmp;}
template <class T> inline void getint(T &num)
{
	bool neg=0;
	num=0;
	char c;
	while ((c=getchar_unlocked()) && (!isdigit(c) && c!='-'));
	if (c=='-')
	{
		neg=1;
		c=getchar_unlocked();
	}
	do num=num*10+c-'0';
	while ((c=getchar_unlocked()) && isdigit(c));
	num*=(neg)?-1:1;
}

void OPEN(string in="input.txt",string out="output.txt")
{
	freopen(in.c_str(),"r",stdin);
	freopen(out.c_str(),"w",stdout);
	return ;
}

//using sokokaleb's template v2.8

ll N,M,ans,mx,norm;
ll cnt[301];
const ll MOD = 1000002013LL;

inline ll f(ll n,ll N) {return (n*N-(n*(n-1))/2)%MOD;}

int main()
{
	getint(N);
	FOR (tc,0,N)
	{
		getint(N);getint(M);
		printf("Case #%d: ",tc+1);
		RESET(cnt,0);ans=0;mx=0;norm=0;

		FOR (i,0,M)
		{
			ll a,b,c;
			getint(a);getint(b);getint(c);
			ll tmp=f(b-a,N)*c;
			tmp%=MOD;
			norm+=tmp;
			if (norm>=MOD) norm-=MOD;
			a=(2*a-1);b=(2*b-1);
			FORN (j,a,b)
			{
				cnt[j]+=c;
				mx=max(cnt[j],mx);
			}
		}

		debug("NORM = %lld\n",norm);
		FORN (i,1,2*N-1) debug("%3lld",cnt[i]);debug("\n");

		// return 0;

		while (mx>0)
		{
			debugln;
			ll localmx=INFLL,fi=-1;
			FORN (i,1,2*N)
			{
				if (cnt[i] && fi==-1)
					fi=i,localmx=INFLL;
				if (fi!=-1 && cnt[i]==0)
				{
					debug("LOCAL = %lld\n",localmx);
					FORN (j,fi,i-1) cnt[j]-=localmx;
					ll tmp=f((i-fi-1)/2,N)*localmx;
					debug("ZZ = %lld\n",f((i-fi-1)/2,N));
					debug("TMP = %lld\n",tmp);
					tmp%=MOD;
					ans=(ans+tmp);
					if (ans>=MOD) ans-=MOD;
					fi=-1;
				}
				localmx=min(cnt[i],localmx);
			}
			mx=0;
			FORN (i,1,N*2-1) mx=max(mx,cnt[i]);
		}
		printf("%lld\n",(norm-ans+MOD)%MOD);
	}
	return 0;
}