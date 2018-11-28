#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); ++e)
typedef long long LL;
typedef pair<int, int> PII;

int tt, n;
map<string, int> ma;
int mac;
string s, t;
bool eng[5000], fr[5000];
vector<int> val[200];
int ei[5000], fi[5000], ec, fc;

int getHash(string &s) {
    auto it = ma.find(s);
    if (it == ma.end()) {
        ma[s] = mac;
        return mac++;
    }
    return it->second;
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> tt;
    REP(test, tt) {
        REP(i, 5000) eng[i] = fr[i] = false;
        cin >> n, n -= 2;
        ma.clear();
        mac = 0;
        getline(cin, s);
        getline(cin, s);
        istringstream iss(s);
        while (iss >> t) {
            eng[getHash(t)] = true;
        }
        getline(cin, s);
        istringstream iss2(s);
        while (iss2 >> t) {
            fr[getHash(t)] = true;
        }
        REP(i, n) {
            val[i].clear();
            getline(cin, s);
            istringstream iss3(s);
            while (iss3 >> t) {
                val[i].pb(getHash(t));
            }
        }
        int ans = 0, best = mac;
        REP(i, mac) if (eng[i] && fr[i])
            ++ans;
        REP(mask, 1 << n) {
            int cur = ans;
            ec = fc = 0;
            REP(i, n) if (mask & (1 << i)) {
                for (int x : val[i]) if (!eng[x]) {
                    eng[x] = true;
                    if (fr[x]) ++cur;
                    ei[ec++] = x;
                }
            } else {
                for (int x : val[i]) if (!fr[x]) {
                    fr[x] = true;
                    if (eng[x]) ++cur;
                    fi[fc++] = x;
                }
            }
            best = min(best, cur);
            REP(i, ec) eng[ei[i]] = false;
            REP(i, fc) fr[fi[i]] = false;
        }
        printf("Case #%d: %d\n", test + 1, best);
    }
	return 0;
}
