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
using namespace std;
typedef long long llong;
typedef pair<int, int> Int2;

const int Maxn = 100000+10;
const int INF = 0x7f7f7f7f;
const int MOD = 1000000007;
const double eps = 1e-10;
const double pi = acos(-1.0);

inline void AddMod(int &x, int det) { x += det; if( x >= MOD ) x -= MOD; }
inline int CompareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }
template<typename T> int sz(const T &a) { return a.size(); }
template<typename T> T str2num(string s) { istringstream i(s); T x; i>>x; return x; }
template<typename T> string x2str(T x) { ostringstream o; o<<x; return o.str(); }

double farm[Maxn];

int main()
{
	int cas;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		double C, F, X, spd=2;
		cin>>C>>F>>X;
		double ans = X/2;
		for(int i=1; ; i++)
		{
			farm[i] = farm[i-1]+C/spd;
			spd += F;
			if( ans < farm[i]+X/spd )
				break;
			ans = farm[i]+X/spd;
		}
		printf("Case #%d: %.8f\n", c, ans);
	}

	return 0;
}
