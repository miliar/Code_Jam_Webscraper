#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define len(x) ((int) (x).size())
#define endl '\n'

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif

using namespace std;

typedef long long int64;
typedef long double ld;
typedef unsigned long long lint;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);
const int N = 1e5;
const int M = 1e9 + 7;

int n, m;
string s[N];
vector<int> p[N];
int ans = 0, total, cnt;

int lcp(int a, int b){
	int ans = 0;
	while (ans < len(s[a]) && ans < len(s[b]) && s[a][ans] == s[b][ans])
		ans++;
	return ans;
}

void append(){
	int sum = total;
	for (int i = 0; i < n; i++){
		for (int j = 1; j < len(p[i]); j++)
			sum -= lcp(p[i][j - 1], p[i][j]);
		if (len(p[i]) == 0)
			return ;
	}
	if (ans < sum)
		ans = sum, cnt = 0;
	if (ans == sum)
		cnt++;
}

void make(int x){
	if (x == m)
		return void (append());
	for (int i = 0; i < n; i++){
		p[i].pb(x);
		make(x + 1);
		p[i].pbk();
	}
}

inline void solve(){
	ans = total = 0;
	cin >> m >> n;
	total = n;
	for (int i = 0; i < m; i++)
		cin >> s[i], total += len(s[i]);
	sort(s, s + m);
	make(0);
	printf("%d %d\n", ans, cnt);
}

int main(){
#if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif
	int t; cin >> t;
	for (int i = 0; i < t; i++){
		printf("Case #%d: ", i + 1);
		solve();
		eprintf("Case #%d: OK!\n", i + 1);
	}
    return 0;
}
