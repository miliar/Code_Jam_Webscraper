#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>  // File RW
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#define FILL(a, v) (memset(a, v, sizeof(a)))
#define foreach(i, Type, v) for(Type::iterator i=v.begin(); i!=v.end(); i++)
#define Rforeach(i, Type, v) for(Type::reverse_iterator i=v.rbegin(); i!=v.rend(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Int2;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const int MOD = 1000000007;
const double eps = 1e-10;
const double pi = acos(-1.0);

inline void AddMod(int &x, int det) { x += det; if( x >= MOD ) x -= MOD; }
inline int CompareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }
template<typename T> int sz(const T &a) { return a.size(); }
template<typename T> T str2num(string s) { istringstream i(s); T x; i>>x; return x; }
template<typename T> string x2str(T x) { ostringstream o; o<<x; return o.str(); }

int solve1(set<double> st_a, set<double> st_b)
{
	int ret = 0;
	Rforeach(ptr, set<double>, st_a)
	{
		if( *st_b.rbegin() > *ptr )
			st_b.erase(*st_b.rbegin());
		else
		{
			ret++;
			st_b.erase(*st_b.begin());
		}
	}
	return ret;
}
int solve2(set<double> st_a, set<double> st_b)
{
	int ret = 0;
	foreach(ptr, set<double>, st_a)
	{
		if( *ptr > *st_b.begin() )
		{
			ret++;
			st_b.erase(*st_b.begin());
		}
		else
			st_b.erase(*st_b.rbegin());
	}
	return ret;
}
int main()
{
	int cas;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		int n;
		double tmp;
		set<double> st_a, st_b;
		cin>>n;
		for(int i=0; i<n; i++)
		{
			cin>>tmp;
			st_a.insert(tmp);
		}
		for(int i=0; i<n; i++)
		{
			cin>>tmp;
			st_b.insert(tmp);
		}
		printf("Case #%d: %d %d\n", c, solve2(st_a, st_b), solve1(st_a, st_b));
	}

	return 0;
}


