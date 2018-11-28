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

set<int> k;

int main() {
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);


    int test = next_int<int>();
    for(int i = 1; i <= test; i++) {
        int n = next_int<int>();

        if(n == 0) {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }

        k.clear();

        int m = 0;
        while(k.size() < 10) {
            m += n;

            int a = m;
            while(a) {
                k.insert(a % 10);
                a /= 10;
            }
        }

        cout << "Case #" << i << ": " << m << "\n";
    }
}