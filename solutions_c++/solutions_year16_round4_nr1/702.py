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

string get_string(char ch, int p) {
    if (p == 0) {
        return string(1, ch);
    } else {
        char ch2;
        if (ch == 'P') {
            ch2 = 'R';
        } else if (ch == 'R') {
            ch2 = 'S';
        } else {
            ch2 = 'P';
        }
        string s1 = get_string(ch, p - 1);
        string s2 = get_string(ch2, p - 1);
        return min(s1 + s2, s2 + s1);
    }
}

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        int n, r, p, s; cin >> n >> r >> p >> s;

        vector<string> vs;
        string str = "RPS";
        for (int i = 0; i < str.size(); ++i) {
            string res = get_string(str[i], n);
            if (count(all(res), 'R') == r &&
                count(all(res), 'P') == p &&
                count(all(res), 'S') == s) {
                vs.push_back(res);
            }
        }
        sort(all(vs));
        if (vs.empty()) {
            vs.push_back("IMPOSSIBLE");
        }

        cout << "Case #" << cs + 1 << ": " << vs[0] << endl;
    }
}
