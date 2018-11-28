#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>
#include <cmath>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

template <typename T>
int numbits(T n) {
    return n ? 1 + numbits(n & (n - 1)) : 0;
}

class timer {
public:
    timer() : t_(clock()) {}
    void restart() { t_ = clock(); }
    float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
    clock_t t_;
};

void run();

int main() {
#ifdef LOCAL_HOST
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    timer t;
#endif
    run();
#ifdef LOCAL_HOST
    // printf("\nElapsed time: %.9f\n", t.elapsed());
#endif
    return 0;
}

bool good(const vector<string>& vs) {
    for (int i = 0; i < vs.size(); ++i) {
        {
            vector<int> idxs;
            for (int j = 0; j < vs.size(); ++j) {
                if (vs[j] == vs[i]) {
                    idxs.push_back(i);
                }
            }
            if (idxs.size() != count(all(vs[i]), '1')) {
                return false;
            }
        }
        {
            vector<int> idxs;
            string str = "";
            for (int j = 0; j < vs.size(); ++j) {
                str += vs[j][i];
            }
            for (int j = 0; j < vs.size(); ++j) {
                bool equal = true;
                for (int k = 0; k < vs.size(); ++k) {
                    if (vs[k][i] != vs[k][j]) {
                        equal = false;
                    }
                }
                if (equal) {
                    idxs.push_back(j);
                }
            }
            if (idxs.size() != count(all(str), '1')) {
                return false;
            }
        }
    }
    return true;
}

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        int n; cin >> n;
        vector<string> vss(n);
        for (int i = 0; i < n; ++i) {
            cin >> vss[i];
        }

        int res = n * n;
        for (int mask = 0; mask < (1 << n * n); ++mask) {
            vector<string> vs = vss;
            int cnt = numbits(mask);
            for (int i = 0; i < (n * n); ++i) {
                if (mask & (1 << i)) {
                    int widx = i / n;
                    int midx = i % n;
                    vs[widx][midx] = '1';
                }
            }
            if (good(vs)) {
                res = min(res, cnt);
            }
        }

        cout << "Case #" << cs + 1 << ": " << res << endl;
    }
}
