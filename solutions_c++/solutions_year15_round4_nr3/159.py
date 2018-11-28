#include <cassert>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(int i = 0;i < (n);++i)

long long MOD = 1000000007;

int T;
unsigned int ar[10010];
map<string, int> m;

int main() {
    cin >> T;
    FOR(itest, T) {
        m.clear();
        int n;
        cin >> n;
        string s;
        getline(cin, s);
        FOR(i, n) {
            getline(cin, s);
            auto start = s.begin();
            for (auto it = s.begin(); ; ++it) {
                if (it == s.end() || *it == ' ') {
                    string t(start, it);
                    if (m.find(t) == m.end()) {
                        int idx = m.size();
                        m[t] = idx;
                        ar[idx] = 0;
                    }
                        //cerr << "[" << t << "] " << m[t] << " " << i << endl;
                    ar[m[t]] |= (1 << i);
                    if (it == s.end()) {
                        break;
                    }
                    start = it + 1;
                }
            }
        }
        int ans = 10000;
        int k = m.size();
        for (int i = 1; i < (1<<n); i += 4) {
            int cur = 0;
            FOR(j, k) {
                cur += (ar[j] & i) && (ar[j] & (~i));
                //cerr << j << " " << ((ar[j] & i) && (ar[j] & (~i))) << endl;
            }
            //cerr << "Cur: " << i << " " << (ar[9]) << " " << cur << endl;
            ans = min(ans, cur);
        }
        cout << "Case #" << (itest + 1) << ": " << ans << endl;
    }
}