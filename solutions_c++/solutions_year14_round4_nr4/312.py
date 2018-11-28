#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)

int n, m, ansmax, ansocc;
vector<string> a;
int ass[16];
char inpp[16];

int trie[100][26];

int calc(const vector<string>& ss) {
    int ans = 1;
    memset(trie, -1, sizeof trie);

    for (auto s : ss) {
        int cur = 0;
        for (auto c : s) {
            int& z = trie[cur][c - 'A'];
            if (z == -1) {
                z = ans++;
            }
            cur = z;
        }
    }

// printf(" %d: ", ans); for (auto s : ss) printf(" %s", s.c_str()); puts("");

    return ans;
}

void calc() {
    int cur = 0;
    forn(j, m) {
        vector<string> s;
        forn(i, n) if (ass[i] == j) s.push_back(a[i]);
        cur += calc(s);
    }
    if (cur == ansmax) ansocc++;
    else if (cur > ansmax) {
        ansmax = cur;
        ansocc = 1;
// printf("new max %d\n", ansmax); forn(i, n) printf(" %d", ass[i]); puts("");
    }
}

void go(int i) {
    if (i == n) {
        forn(j, m) {
            bool was = false;
            forn(k, n) was |= ass[k] == j;
            if (!was) return;
        }
        calc();
        return;
    }
    forn(j, m) {
        ass[i] = j;
        go(i + 1);
    }
}

int main() {
    int __;
    scanf("%d", &__);
    forn(_, __) {
        a.clear();
        scanf("%d%d", &n, &m);
        forn(i, n) scanf("\n%s", inpp), a.push_back(inpp);
        ansmax = ansocc = 0;
        go(0);
        printf("Case #%d: %d %d\n", _+1, ansmax, ansocc);
    }
    return 0;
}
