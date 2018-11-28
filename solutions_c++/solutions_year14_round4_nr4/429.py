#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;

char str[10][20];

int a[10];
int m, n;

int const N = 10000;
int const M = 26;
struct Trie_Node {
    int id;
    Trie_Node *next[26];
    void init() {
         id = -1;
         memset(next, NULL, sizeof next);
    }
} trie[N * M], root;
int tidx, cnt;
int insert(char* s) {
    int i, j;
    Trie_Node *p = &root;
    for (i = 0; s[i]; ++i) {
        if (s[i] <= 'Z') j = s[i] - 'A';
        if (p -> next[j] == NULL) {
            trie[tidx].init();
            p -> next[j] = &trie[tidx++];
        }
        p = p -> next[j];
    }
    if (p -> id == -1) p -> id = cnt++;
    return p -> id;
}
void init() {
    root.init();
    tidx = cnt = 0;
}

int ans, acc;

void dfs(int d) {
	if (d == m) {
		int t = 0;
		bool vis[5]; rep(i, 5) vis[i] = 0;
		rep(i, n) {
			init();
			rep(j, m) if (a[j] == i) {
				if (!vis[i]) {
					vis[i] = 1;
					++t;
				}
				insert(str[j]);
			}
			t += tidx;
		}
		//rep(i, m)cout<<a[i]<<" ";cout<<endl;
		//cout<<t<<endl;
		if (t == ans) ++acc;
		else if (t > ans) {
			ans = t;
			acc = 1;
		}
		return;
	}
	rep(i, n) {
		a[d] = i;
		dfs(d + 1);
	}
}

int main() {
#if 1
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("D-large.in", "r", stdin);
	freopen("D-ans.txt", "w", stdout);
#endif
	int T, ca = 1;
	for (scanf("%d", &T); T--; ) {
		cerr<<T<<endl;
		scanf("%d%d", &m, &n);
		rep(i, m) scanf(" %s", str[i]);
		ans = -1, acc = 1;
		dfs(0);
		printf("Case #%d: %d %d\n", ca++, ans, acc);
	}
	return 0;
}


