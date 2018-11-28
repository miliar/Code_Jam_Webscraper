#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = 111;
const long long INF = 1e9 + 19;
const int CNT_IT = 5000;

int n;
vector < int > e[N];
char s[N];
char word[N];
bool use[N];
int cnt[N];
int p[N];
bool open[N];
char t[N];

void read() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		e[i].clear();
	for (int i = 0; i < n; i++) {
		int x;
		scanf("%d", &x); x--;
		p[i] = x;
		if (x != -1) {
			e[x].pb(i);
		}
	}
	scanf("%s", s);
}

void dfs1(int v) {
	use[v] = 1;
	cnt[v] = 1;
	for (auto u: e[v]) {
		if (!use[u]) {
			dfs1(u);
		}
		cnt[v] += cnt[u];
	}
}

void solve() {
	srand(time(NULL));
	int test = 0;
	memset(use, 0, sizeof(use));
	for (int i = 0; i < n; i++)
		if (!use[i])
			dfs1(i);
		
	scanf("%d", &test);
	for (int tt = 0; tt < test; tt++) {
		int good = 0;
		scanf("%s", word);
		int len = strlen(word);	
		for (int gg = 0; gg < CNT_IT; gg++) {
			for (int i = 0; i < n; i++)
				open[i] = p[i] == -1;
			for (int i = 0; i < n; i++) {
				vector < pair < int, int > > g;
				int sum = 0;
				for (int j = 0; j < n; j++)
					if (open[j]) {
						g.pb(mp(j, cnt[j]));
						sum += cnt[j];
					}
				int rnd = rand() % sum;
				int cur = 0;
				for (; cur < (int)g.size() && rnd >= g[cur].sc; cur++) 
					rnd -= g[cur].sc;
				assert(cur < (int)g.size());
				int v = g[cur].fr;
				t[i] = s[v];
				open[v] = 0;
				for (auto u: e[v])
					open[u] = 1;
			}
			bool flag = 0;
			for (int i = 0; !flag && i + len <= n; i++) {
				bool f = 1;
				for (int j = 0; j < len; j++)
					f &= t[i + j] == word[j];
				flag |= f;
			}
			good += flag;
		}		
		printf("%.2f ", good * 1.0 / CNT_IT);
	}
	puts("");
}

void stress() {

}

int main(){
#ifdef MY_DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
		scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
			db(tt);
			printf("Case #%d: ", tt + 1);
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}


