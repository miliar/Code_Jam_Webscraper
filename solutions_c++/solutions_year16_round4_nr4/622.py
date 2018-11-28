#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FOREACH(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }


typedef pair<int, int> P;
const int N = 100;
int p[N], dp[N];

const int INF = (int) 1E9;

struct E {
    int to, cap, rev;
    E() {}
    E(int to, int cap, int rev) : to(to), cap(cap), rev(rev) {}
};

struct MaxFlow {
    vector<E> G[N];
    int level[N], iter[N];

    void add_edge(int from, int to, int cap) {
        G[from].push_back(E(to, cap, G[to].size()));
        G[to].push_back(E(from, 0, G[from].size() - 1));
    }
    
    void bfs(int s) {
        memset(level, -1, sizeof(level));
        queue<int> que;
        level[s] = 0;
        que.push(s);
        while (!que.empty()) {
            int v = que.front(); que.pop();
            for (int i = 0; i < G[v].size(); ++i) {
                E &e = G[v][i];
                if (e.cap > 0 && level[e.to] < 0) {
                    level[e.to] = level[v] + 1;
                    que.push(e.to);
                }
            }
        }
    }
    
    int dfs(int v, int t, int f) {
        if (v == t) return f;
        for (int &i = iter[v]; i < G[v].size(); ++i) {
            E &e = G[v][i];
            if (e.cap > 0 && level[v] < level[e.to]) {
                int d = dfs(e.to, t, tmin(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    G[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }
    
    int max_flow(int s, int t) {
        int ans = 0;
        for (;;) {
            bfs(s);
            if (level[t] < 0) return ans;
            memset(iter, 0, sizeof(iter));
            int f;
            while ((f = dfs(s, t, INF)) > 0) {
                ans += f;
            }
        }
        return ans;
    }
};

bool check(int n) {
	REPU(i, 0, n) {
		if (dp[i] == (1 << n) - 1) continue;
		MaxFlow mf;
		int st = n + n + 1, en = st + 1;
		int tot = 0;
		REPU(j, 0, n) if (dp[i] & (1 << j)) {
			mf.add_edge(st, j, 1);
			tot++;
		}
		REPU(k, 0, n) if (k != i) {
			mf.add_edge(k + n, en, 1);
			REPU(j, 0, n) if (dp[k] & (1 << j)) {
				mf.add_edge(j, k + n, 1);
			}
		}
		if (mf.max_flow(st, en) == tot) return false;
	}
	return true;
}

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	
	int nTest, n; string s;

	cin >> nTest;
	REPU(it, 1, nTest + 1) {
		cin >> n;
		vector<P> pos;
		MEM(p, 0);
		REPU(i, 0, n) {
			cin >> s;
			REPU(j, 0, n) {
				if (s[j] == '0') pos.push_back({i, j});
				else p[i] |= 1 << j;
			}
		}
		printf("Case #%d: ", it);
		REPU(i, 0, n) dp[i] = p[i];
		if (check(n)) {
			puts("0"); continue;
		}
		int m = pos.size();
		int ans = n * n;
		REPU(i, 1, 1 << m) {
			int ret = 0;
			REPU(j, 0, n) dp[j] = p[j];
			REPU(j, 0, m) if (i & (1 << j)) {
				dp[pos[j].first] |= 1 << pos[j].second;
				ret++;
			}
			if (check(n)) amin(ans, ret);
		}
		printf("%d\n", ans);
	}
	
	return 0;
}
