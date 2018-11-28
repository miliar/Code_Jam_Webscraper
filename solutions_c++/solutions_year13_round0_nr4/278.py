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
#define MAX(_a,_b) (((_a)>(_b))?(_a):(_b))
#define MIN(_a,_b) (((_a)<(_b))?(_a):(_b))
 
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

//using sokokaleb's template v2.7

int dp[1<<20];
int key[205];
int n,type[25],t;
int keys[25][205];

int f(int mask)
{
	int &ret=dp[mask];
	if (ret!=-1) return ret;
	if (mask==(1<<t)-1) return ret=1;
	ret=0;
	int tmpk[205];
	RESET(tmpk,0);
	FOR (i,0,t)
		if (mask&(1<<i))
		{
			--tmpk[type[i]];
			FOR (j,0,205)
				tmpk[j]+=keys[i][j];
		}
	FOR (j,0,205) tmpk[j]+=key[j];
	FOR (i,0,t)
		if (!(mask&(1<<i)) && tmpk[type[i]]>0)
			ret|=f(mask|(1<<i));
	return ret;
}

void bt(int mask)
{
	if (mask==(1<<t)-1)
	{
		puts("");
		return ;
	}
	int tmpk[205];
	RESET(tmpk,0);
	FOR (i,0,t)
		if (mask&(1<<i))
		{
			--tmpk[type[i]];
			FOR (j,0,205)
				tmpk[j]+=keys[i][j];
		}
	FOR (j,0,205) tmpk[j]+=key[j];
	FOR (i,0,t)
		if (!(mask&(1<<i)) && tmpk[type[i]]>0 && f(mask|(1<<i)))
		{
			printf(" %d",i+1);
			bt(mask|(1<<i));
			return ;
		}
	return ;
}

int main()
{
	getint(n);
	FOR (tc,0,n)
	{
		getint(n);getint(t);
		RESET(key,0);
		FOR (i,0,n)
		{
			getint(n);
			--n;++key[n];
		}
		FOR (i,0,t)
		{
			getint(type[i]);--type[i];
			getint(n);RESET(keys[i],0);
			FOR (j,0,n)
			{
				getint(n);--n;
				++keys[i][n];
			}
		}
		RESET(dp,-1);
		printf("Case #%d:",tc+1);
		if (f(0)==1) bt(0);
		else puts(" IMPOSSIBLE");
	}
	return 0;
}