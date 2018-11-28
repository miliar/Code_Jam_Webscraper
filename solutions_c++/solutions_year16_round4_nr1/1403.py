#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
#include <list>

using namespace std;
typedef long long ll;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef pair<string, int> PSI;
typedef pair<string, string> PSS;
typedef pair<PII, int> PIP;
const int mod = 1000000007;
const double pi = acos(-1);
const int N = 5000;
PII f[15][3];
// r = first, s = second, p = (1<<n)-r-s
void precalc() {
    f[1][0] = PII(1, 1);
    f[1][1] = PII(0, 1);
    f[1][2] = PII(1, 0);
    for(int k = 1; k < 12; k ++) {
        for(int w = 0; w < 3; w ++) {
            for(int w2 = w + 1; w2 < 3; w2 ++) {
                int nextr = f[k][w].first + f[k][w2].first;
                int nexts = f[k][w].second + f[k][w2].second;
                int nextw = 0;
                if (w + w2 == 1) nextw = 0;
                if (w + w2 == 2) nextw = 2;
                if (w + w2 == 3) nextw = 1;
                f[k+1][nextw] = PII(nextr, nexts);
            }
        }
    }
}
// r = 0, s = 1, p = 2
// (rp)->p, (ps)->s, (sr)->r
// (02)->2, (12)->1, (01)->0
int n, r, p, s, k;
bool ok(int w) {
    PII p = f[k][w];
    return p.first == r && p.second == s;
}
string str;
void print(int k, int w) {
    if (k == 0) return;
    PII p = f[k][w];
    if (w == 0) {
        str.push_back('R');
        str.push_back('S');
        for(int i = 1; i <= k-1; i++) print(i, 1);
    } else if (w == 1) {
        str.push_back('P');
        str.push_back('S');
        for(int i = 1; i <= k-1; i++) print(i, 2);
    } else {
        str.push_back('P');
        str.push_back('R');
        for(int i = 1; i <= k-1; i++) print(i, 0);
    }
}

void sortstr(int idx, int k) {
    if (k == 0) return;
    int L = 1<<(k-1);
    sortstr(idx, k-1);
    sortstr(idx+L, k-1);
    string sub1 = str.substr(idx, L);
    string sub2 = str.substr(idx+L, L);
    if (sub1>sub2) {
        for(int i = 0;i<L;i++) str[i + idx] = sub2[i];
        for(int i = 0;i<L;i++) str[i + idx + L] = sub1[i];
    }
}
void solve(int ncase) {
    cout << "Case #" << ncase << ": ";
    cin >> k >> r >> p >> s;

    for(int i = 0; i < 3; i++) {
        if (ok(i)) {
            str="";
            print(k, i);
            sortstr(0, k);
            cout << str << endl;
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}
int main() {
    //ios::sync_with_stdio(false);
    //cout << std::fixed << setprecision(16);
#ifdef _zzz_
    //freopen("in.txt", "r", stdin);
    //freopen("A-small-practice.in", "r", stdin);
    //freopen("A-large-practice.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    clock_t start = clock();
#endif
    int T = 1;
    precalc();
    cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
#ifdef _zzz_
    //cerr << std::fixed << setprecision(16) <<"spend " << (clock() -start )*1.0/CLOCKS_PER_SEC << " s" << endl;
#endif
}
