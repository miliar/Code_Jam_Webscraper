//I hate this town, bacause it's too filled with memories I'd rather forget.
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

//Two becomes one,and it through all eternity.
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
int value[1000];
char s[1001][1001];
int t[1001][1001];
int n, m;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("temp.in", "r", stdin); freopen("temp.ans", "w", stdout);
#endif
value['<'] = 1; value['>'] = 2;
value['^'] = 4; value['v'] = 8;
int TestCase; cin >> TestCase;
for (int ti = 1; ti <= TestCase; ti++){
	memset(t, 0, sizeof(t));
	printf("Case #%d: ", ti);
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) scanf("%s", &s[i][1]);
	for (int i = 1; i <= n; i++){
		int p = 1;
		while(s[i][p] == '.') p++;
		t[i][p] |= 1;
		p = m;
		while(s[i][p] == '.') p--;
		t[i][p] |= 2;
	}
	for (int i = 1; i <= m; i++){
		int p = 1;
		while(s[p][i] == '.') p++;
		t[p][i] |= 4;
		p = n;
		while(s[p][i] == '.') p--;
		t[p][i] |= 8;
	}
	int ans = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (t[i][j] == 15){
				puts("IMPOSSIBLE");
				goto end;
			}
			else{
				if (t[i][j] & value[s[i][j]]) ans++;
			}
	cout << ans << endl;
end:;
}    

}
