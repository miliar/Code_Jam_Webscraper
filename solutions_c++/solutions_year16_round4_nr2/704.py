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

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        int n, k; cin >> n >> k;
        vector<double> ps(n);
        for (int i = 0; i < n; ++i) {
            cin >> ps[i];
        }

        double res = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            if (numbits(mask) != k) {
                continue;
            }
            vector<double> p;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    p.push_back(ps[i]);
                }
            }
            double subres = 0;
            for (int submask = 0; submask < (1 << k); ++submask) {
                if (numbits(submask) != k / 2) {
                    continue;
                }
                double ppp = 1.0;
                for (int i = 0; i < p.size(); ++i) {
                    if (submask & (1 << i)) {
                        ppp *= p[i];
                    } else {
                        ppp *= (1.0 - p[i]);
                    }
                }
                subres += ppp;
            }
            res = max(subres, res);
        }

        cout << "Case #" << cs + 1 << ": ";
        printf("%.9f\n", res);
    }
}
