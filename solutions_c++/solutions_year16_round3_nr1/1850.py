#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstring>
#include <cstdarg>
#include <cstdio>
#include <random>
#include <cmath>
#include <ctime>
#include <functional>
#include <algorithm>
#include <complex>
#include <numeric>
#include <limits>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <array>
#include <list>
#include <map>
#include <set>
using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) int((a).size())
#define MP(x, y) make_pair((x),(y))
#define FI first
#define SE second
#define LOWB(x) (x & (-x))
#define UNIQUE(a) sort(ALL(a)), (a).erase(unique(ALL(a)), (a).end())
#define HEIGHT(n) (sizeof(int) * 8 - __builtin_clz(n)) //height of range n segment tree
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
template<class T> inline T min(T a, T b, T c) {return min(min(a,b),c);}
template<class T> inline T min(T a, T b, T c, T d) {return min(min(a,b),min(c,d));}
template<class T> inline T max(T a, T b, T c) {return max(max(a,b),c);}
template<class T> inline T max(T a, T b, T c, T d) {return max(max(a,b),max(c,d));}
const int INF = 1e9;
const ll INF_LL = 4e18;
const double pi = acos(-1.0);
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
/*-----------------------------------*/
int n, cnt[26];

int check1(int tot) {
    for (int i=0; i<n; i++) if (cnt[i]) {
        if ((cnt[i] - 1) * 2 > (tot - 1)) continue;
        bool flag = true;
        for (int j=0; j<n; j++) if (cnt[j] && j != i) {
            if (cnt[j] * 2 > tot - 1) {
                flag = false;
                break;
            }
        }
        if (flag) return i;
    }
    return -1;
}

pii check2(int tot) {
    for (int i=0; i<n; i++) if (cnt[i]) {
        for (int j=i+1; j<n; j++) if (cnt[j]) {
            if ((cnt[i] - 1) * 2 > (tot - 2)) continue;
            if ((cnt[j] - 1) * 2 > (tot - 2)) continue;
            bool flag = true;
            for (int k=0; k<n; k++) if (cnt[k] && k!=i && k!=j) {
                if (cnt[k] * 2 > tot - 2) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return make_pair(i, j);
            }
        }
    }
    return make_pair(-1, -1);
}

void solve() {
    int tot = 0;
    vector<string> ans;
    for (int i=0; i<26; i++) tot += cnt[i];

    while (tot) {
        int p1 = check1(tot);
        if (p1 != -1) {
            string str = "";
            str += 'A' + p1;
            ans.push_back(str);
            cnt[p1]--;
            tot--;
        } else {
            pii p2 = check2(tot);
            assert(p2.first != -1);
            cnt[p2.first]--;
            cnt[p2.second]--;
            tot -= 2;
            string str = "";
            str += 'A' + p2.first;
            str += 'A' + p2.second;
            ans.push_back(str);
        }
    }
    for (auto s: ans) printf(" %s", s.c_str());
    printf("\n");
}

int main() {
//    freopen("test.in", "r", stdin);
    int cases;
    cin >> cases;
    for (int cas=1; cas <= cases; cas++) {
        cin >> n;
        for (int i=0; i<n; i++) cin >> cnt[i];
        printf("Case #%d:", cas);
        solve();
    }
    return 0;
}
