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
#define PII pair<int, LL>
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
map<int, LL> c;
stack<PII > S;
LL ans;
int main()
{
freopen("temp.in", "r", stdin); freopen("temp.out", "w", stdout);
int T; scanf("%d", &T);
for (int ti = 1; ti <= T; ti++){    
	printf("Case #%d: ", ti);
	c.clear(); while(S.size()) S.pop(); ans = 0;
	LL n;
	int m;
	scanf("%lld%d", &n, &m);
	for (int i = 1; i <= m; i++){
		int l, r, v;
		scanf("%d%d%d", &l, &r, &v);
		ans += (((LL)n * 2 - (r - l) + 1) * (r - l) / 2) % 1000002013 * (LL)v % 1000002013;
		ans %= 1000002013;
		c[l] += v;
		c[r] -= v;
	}
	fr(x, c){
		int pos = x->first; LL num = x->second;
		if (num > 0)
			S.push(MP(pos, num));
		else{
			while(num != 0){
				PII t = S.top();
				S.pop();
				if (t.second > -num)
					S.push(MP(t.FR, t.SC + num));
				t.SC = min(t.SC, -num);
				ans = (ans - (((LL)(2 * n - (pos - t.FR) + 1) * (pos - t.FR) / 2) % 1000002013 * t.SC) % 1000002013) % 1000002013;
				num += t.SC;
			}
			
		}
	}
	cout << (ans + 1000002013 ) % 1000002013<< endl;

	}
	puts("");
}
