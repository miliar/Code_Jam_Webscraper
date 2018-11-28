#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <sstream>
#include <iomanip>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 205;
int Tc, n;
vector <string> s[N];
vector <int> a[N];
bool lhs[1000000], rhs[1000000];
set <string> all;
map <string, int> ind;

vector <string> getAll(const string &s) {
    istringstream iss(s);
    vector <string> res;
    string cur;
    while (iss >> cur) {
        res.push_back(cur);
        all.insert(cur);
    }
    return res;
}

void addAll(const vector <int> &v, bool r[]) {
    for (const int u : v) {
        r[u] = 1;
    }
}

int main() {
    cin >> Tc;
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        cin >> n;
        string cur;
        getline(cin, cur);
        all.clear();
        rep (i, n) {
            getline(cin, cur);
            s[i] = getAll(cur);
        }
        ind.clear();
        int cnt = 0;
        for (string cur : all) {
            ind[cur] = cnt++;
        }
        rep (i, n) {
            a[i].clear();
            rep (j, s[i].size()) {
                a[i].push_back(ind[s[i][j]]);
            }
        }
        int ans = (int)1e9;
        rep (mask, 1 << (n - 2)) {
            fill(lhs, lhs + all.size(), 0);
            fill(rhs, rhs + all.size(), 0);
            addAll(a[0], lhs);
            addAll(a[1], rhs);
            rep (i, n - 2) {
                if (mask & 1 << i) {
                    addAll(a[i + 2], lhs);
                } else {
                    addAll(a[i + 2], rhs);
                }
            }
            int res = 0;
            rep (i, all.size()) {
                if (lhs[i] && rhs[i]) {
                    res++;
                }
            }
            if (res < ans) ans = res;
        }
        fprintf(stderr, "%d\n", ri + 1);
        printf("%d\n", ans);
    }
}

