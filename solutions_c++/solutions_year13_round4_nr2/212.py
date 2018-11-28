#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

//kAc
const double pi = acos(-1.0), eps = 1e-9;
const int dx[8] = {1, -1, 0, 0, 1, 1, -1, -1};
const int dy[8] = {0, 0, 1, -1, 1, -1, -1, 1};
const int MO = (int)(1e9 + 7);

#define ALL(x) x.begin(), x.end()
#define fr(x, E) for (__typeof(E.begin()) x = E.begin(); x != E.end(); x++)
#define MP make_pair
#define PB push_back
#define FR first
#define SC second
#define ERR cerr << "ERROR" << endl
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PIII pair<PII, int>
#define PDI pair<double, int>
#define PID pair<int, double>
#define SZ(a) (int)((a).size())
#define VEC vector
#define STR string
#define ISS istringstream
#define OSS ostringstream
#define CLR(a, b) memset(a, b, sizeof(a))
#define gmin(a, b) { if (b < a) a = b; }
#define gmax(a, b) { if (b > a) a = b; }

using namespace std;
LL judge1(LL x, LL n)
{
	if (x == 0) return 0; else return n / 2 + judge1(x - 1 >> 1, n / 2);
}
LL judge2(LL x, LL n)
{
	if (x == n - 1) return 0; else return n / 2 + judge2(x + 1 >> 1, n / 2);
}
int main()
{
freopen("temp.in", "r", stdin);
 freopen("temp.out", "w", stdout);
int T; scanf("%d", &T);
for (int ti = 1; ti <= T; ti++){    
	printf("Case #%d: ", ti);
	LL n, p; cin >> n >> p;
	LL l = 0, r = (1ll << n) - 1;
	while (l <= r){
		LL m = l + r >> 1;
		if (judge1(m, 1ll << n) >= p) r = m - 1;
		else l = m + 1;
	}
	cout << " " << r;
	l = 0; r = (1ll << n) - 1;
	while (l <= r){
		LL m = l + r >> 1;
		if (judge2(m, 1ll << n) < ((1ll << n) - p)) r = m - 1;
		else l = m + 1;
	}
	cout << " " << r;
	puts("");
	
}
}
