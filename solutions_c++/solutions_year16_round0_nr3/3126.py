#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iomanip>
#include <ctime>
using namespace std;

template <typename T>
T next_int() {
    T x = 0, p = 1;
    char ch;
    do { ch = getchar(); } while(ch <= ' ');
    if (ch == '-') {
        p = -1;
        ch = getchar();
    }
    while(ch >= '0' && ch <= '9') {
        x = x * 10 + (ch - '0');
        ch = getchar();
    }
    return x * p;
}

const int max_n = (int)1e6 + 228;
const int max_int = (int)1e9 + 228;

int n, m;

long long ans[max_n];

string a;

void go(int p) {
    if(!m) exit(0);

    if(p == n) {
        int ok = 0;
        for(int i = 2; i <= 10; i++) {
            long long b = 0;
            for(long long j = n - 1, st = 1; j >= 0; j--, st *= i) {
                b += st * (a[j] - '0');
            }

            for(long long j = 2; j * j <= b; j++) {
                if(b % j == 0) { ok++, ans[i] = j; break; }
            }
        }
        if(ok != (10 - 2 + 1)) return;

        cout << a << " ";
        for(int i = 2; i <= 9; i++) cout << ans[i] << " ";
        cout << ans[10] << "\n";
        m--;
        return;
    }

    if(p == 0 || p == n - 1) {
        a += '1';
        go(p + 1);
        a.resize(a.size() - 1);
        return;
    }

    a += '1';
    go(p + 1);
    a.resize(a.size() - 1);

    a += '0';
    go(p + 1);
    a.resize(a.size() - 1);
}

int main() {
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);

    int test = next_int<int>();

    n = next_int<int>();
    m = next_int<int>();

    puts("Case #1:");
    go(0);
}