#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,n) for(int i=1;i<=(n);i++)
#define FORD(i,n) for(int i=(n);i>=1;i--)

#define SZ(x) ((int)x.size())
#define CC(a,x) memset(a,x,sizeof(a))
#define TWO(x) ((LL)1<<(x))

using namespace std;

int T, n;
int eng[4001];
int fre[4001];
int cnt;
map<string, int> has;

vector<string> getwords() {
    string line;
    string buf;
    vector<string> words;
    getline(cin, line);
    stringstream ss(line);
    while (ss >> buf) {
        words.push_back(buf);
    }
    return words;
}

vector<string> words;
vector<int> lines[201];
int ans;

void dfs(int u) {
    if (u >= n) {
        int cnt = 0;
        REP(i, 4000) if (eng[i] > 0 && fre[i] > 0) {
            cnt++;
        }
        ans = min(ans, cnt);
        return;
    }
    int m = lines[u].size();
    REP(i, m) {
        eng[lines[u][i]] += 1;
    }
    dfs(u + 1);
    REP(i, m) {
        eng[lines[u][i]] -= 1;
    }
    REP(i, m) {
        fre[lines[u][i]] += 1;
    }
    dfs(u + 1);
    REP(i, m) {
        fre[lines[u][i]] -= 1;
    }
}

void solve() {
    cnt = 0;
    ans = 4000;
    has.clear();
    scanf("%d\n", &n);
    n -= 2;
    REP(i, n) lines[i].clear();
    CC(eng, 0);
    CC(fre, 0);
    words = getwords();
    int m;
    m = words.size();
    REP(j, m) {
        if (has.find(words[j]) == has.end()) {
            has[words[j]] = (cnt++);
        }
        eng[has[words[j]]] = 1;
    }
    words = getwords();
    m = words.size();
    REP(j, m) {
        if (has.find(words[j]) == has.end()) {
            has[words[j]] = (cnt++);
        }
        fre[has[words[j]]] = 1;
    }
    REP(i, n) {
        words = getwords();
        m = words.size();
        REP(j, m) {
            if (has.find(words[j]) == has.end()) {
                has[words[j]] = (cnt++);
            }
            lines[i].push_back(has[words[j]]);
        }
    }
    dfs(0);
    printf("%d", ans);
}

int main() {
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
