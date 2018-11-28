#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cassert>

const char* input_file = "B-large.in";
//const char* input_file = "input.txt";
const int Mod = 1000002013;

using namespace std;


int N;
long long P;
long long x;

long long calc(int n, long long p) {
    if (p == 0) {
        return -1;
    }
    int k = 0;
    while (p > 0) {
        p /= 2; ++k;
    }

    k = n - k + 1;

    long long r = 1;
    while (k > 0) {
        r *= 2;
        k -= 1;
    }

    return x - r;
}

void solve() {
    cin >> N >> P;
    int t = N;
    x = 1;
    while (t > 0) {
        x *= 2;
        t -= 1;
    }
    long long a1 =  x - 2 - calc(N, x - P);
    long long a2 = calc(N, P);
    assert(a1 >= 0 && a1 < x);
    assert(a2 >= 0 && a2 < x);
    cout << a1 << " " << a2;
}

int main() {
    freopen(input_file, "r", stdin);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

