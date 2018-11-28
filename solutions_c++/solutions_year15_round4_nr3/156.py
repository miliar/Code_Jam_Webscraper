// /\||/\||
//
//
//////////////////////
// Program: 
// Written By Alireza Farhadi (LGM)
//////////////////////
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cassert>
#include <csignal>
#include <cmath>
#include <array>
#include <queue>
#include <stack>
#include <string>
#include <regex>
#include <set>
#include <map>
#include <tuple>
#include <list>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

using namespace std;
#ifdef _TEST
#define testdo(x) x
#else
#define testdo(x)
#endif
#define show(x) testdo(cerr<<((#x))<<" = "<<((x))<<" "<<endl)
#define bit(a,b) (((a)>>(b))&1)
#define gt(x,i) (get<((i))>(((x))))
#define ALL(x) ((x)).begin(),((x)).end()
#define Mt make_tuple
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define bcntll(x) ((__builtin_popcountll(x)))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)
#define list _list

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T gcd(T x,T y) { return y?gcd(y,x%y):x;}
namespace std{ template<class T,class U> struct hash<pair<T,U>> {
	inline size_t operator() (const pair<T,U> & p) const { return hash<T>()(p.first)*701+hash<U>()(p.second);}
};}

typedef long long ll;
typedef pair<int,int> pie;
typedef tuple<int,int,int> trip;
typedef complex<double> point;

const double eps=1e-8;

int t,n;
string list[100];
vector<string> words[100];
map<string,int> cnt[2];
int res;
void go(int a,int now=0)
{
	if (now>=res) return ;
	if (a>=n)
	{
		res=now;
		return ;
	}
	int s=(a==1?1:0),e=(a==0?0:1);
	for (int i=s;i<=e;i++)
	{
		int ns=now;
		for (auto & x:words[a])
		{
			cnt[i][x]++;
			if (cnt[i][x]==1 && cnt[i^1].find(x)!=cnt[i^1].end())
				ns++;
		}
		go(a+1,ns);
		for (auto & x:words[a])
		{
			cnt[i][x]--;
			if (cnt[i][x]==0) cnt[i].erase(x);
		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		show(tc);
		cin>>n;
		string _;
		getline(cin,_);
		for (int i=0;i<n;i++)
		{
			getline(cin,list[i]);
			words[i].clear();
			string s;
			istringstream sin(list[i]);
			while (sin>>s)
				words[i].push_back(s);
		}
		cnt[0].clear();
		cnt[1].clear();
		res=(1<<20);
		go(0);
		cout<<"Case #"<<tc<<": "<<res<<endl;
	}
	return 0;
}
