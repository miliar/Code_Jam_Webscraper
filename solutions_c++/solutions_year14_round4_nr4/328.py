#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <functional>
#include <numeric>
#include <sstream>
#include <complex>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))

using namespace std;

int to[1111];

int bn;
int bor[11111][33];

inline void add(const char* s) {
    int cur = 0;
    for (int i = 0; s[i]; ++i) {
        if (!bor[cur][s[i] - 'A']) {
            bor[cur][s[i] - 'A'] = ++bn;
            memset(bor[bn], 0, sizeof(bor[bn]));
        }
        cur = bor[cur][s[i] - 'A'];
    }
}

void rec(int i, vector<string>& s, int n, int& best, int& bc) {
    if (i == (int)s.size()) {
        int sum = 0;
        int bad = 0;
        for (int sj = 0; sj < n; ++sj) {
            bn = 0;
            memset(bor[0], 0, sizeof(bor[0]));
            int fnd = 0;
            for (int j = 0; j < (int)s.size(); ++j) {
                if (to[j] == sj) {
                    add(s[j].c_str());
                    fnd = 1;
                }
            }
            if (!fnd) {
                bad = 1;
                break;
            }
            sum += bn + 1;
        }
        if (bad) return;
        if (sum > best) {
            best = sum;
            bc = 1;
        } else
        if (sum == best) {
            ++bc;
        }
        return;
    }
    for (int j = 0; j < n; ++j) {
        to[i] = j;
        rec(i + 1, s, n, best, bc);
    }
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    
    int T;
    int it = 0;
    cin >> T;
    while (T--) {
        ++it;

        int M, N;
        cin >> M >> N;
        vector<string> s(M);
        for (int i = 0; i < M; ++i) {
            cin >> s[i];
        }

        int best = 0, bc = 0;
        rec(0, s, N, best, bc);        

        cout << "Case #" << it << ": " << best << " " << bc << endl;
    }
    
    
    return 0;
}
