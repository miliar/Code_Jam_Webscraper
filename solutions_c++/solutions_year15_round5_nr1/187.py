#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <utility>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>

using namespace std;

typedef long long LL;
template<class T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<class T> inline T Sqr(const T& x) { return x * x; }



const int maxn = 1000 * 1000 + 1000;
vector<int> e[maxn];
vector<int> p;
vector<LL> s;
map<LL, vector<int>> sal2id;
int now[maxn];
int nowsize = 0;
int avail[maxn];
LL L, R;

void Add(int v) {
    avail[v] = 1;
    if (now[p[v]] && !now[v]) {
        now[v] = 1;
        ++nowsize;
        for (size_t i = 0; i < e[v].size(); ++i) {
            if (avail[e[v][i]] && !now[e[v][i]]) {
                Add(e[v][i]);
            }
        }
    }
}

void Remove(int v) {
    avail[v] = 0;
    if (now[v]) {
        now[v] = 0;
        --nowsize;
        for (size_t i = 0; i < e[v].size(); ++i) {
            if (now[e[v][i]]) {
                Remove(e[v][i]);
            }
        }
    }
}


void Solution() {
    LL n, d;
    cin >> n >> d;
    for (int i = 0; i < n; ++i) {
        e[i].clear();
    }
    memset(now, 0, sizeof(now));
    nowsize = 0;
    memset(avail, 0, sizeof(avail));
    s.resize(n);
    LL as, cs, rs;
    cin >> s[0] >> as >> cs >> rs;
    LL am, cm, rm;
    vector<LL> m(n);
    cin >> m[0] >> am >> cm >> rm;
    p.resize(n);
    sal2id.clear();
    for (int i = 1; i < n; ++i) {
        s[i] = (s[i - 1] * as + cs) % rs;
        m[i] = (m[i - 1] * am + cm) % rm;
        p[i] = m[i] % i;
        e[p[i]].push_back(i);
        sal2id[s[i]].push_back(i);
    }
    now[0] = 1;
    avail[0] = 1;
    nowsize = 1;
    L = s[0] - d;
    R = s[0];
    for (int i = 1; i < n; ++i) {
        if (s[i] <= s[0] && s[i] >= s[0] - d) {
            Add(i);
        }
    }
    int mx = nowsize;
    for (LL l = s[0] - d; l < s[0]; ++l) {
        LL r = l + d + 1;
        L = l + 1;
        R = r;
        vector<int>& toAdd = sal2id[r];
        for (size_t i = 0; i < toAdd.size(); ++i) {
            Add(toAdd[i]);
        }
        vector<int>& toRemove = sal2id[l];
        for (size_t i = 0; i < toRemove.size(); ++i) {
            Remove(toRemove[i]);
        }
        mx = max<int>(mx, nowsize);
    }
    cout << mx << endl;
}


int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        float startTime = clock() / CLOCKS_PER_SEC;
        cout << "Case #" << i + 1 << ": ";
        Solution();
        float endTime = clock() / CLOCKS_PER_SEC;
        cerr << "Test #" << i + 1 << ": elapsed time is " << endTime - startTime;
        cerr << endl;
    }

    return 0;
}


