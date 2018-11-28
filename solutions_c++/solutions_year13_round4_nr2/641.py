#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <queue>
#include <vector>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
using namespace std;
long long n, p, m;
long long a[1200], b[1200];
int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        cin >> n >> p;
        m = (1<<n);
        long long a1 = 0, a2 = 0;
        long long a3 = 2;
        long long t1 = (1<<(n-1));
        long long t2 = 0;
        while (t2+t1 < p) {
            t2 += t1;
            t1 /= 2;
            a1 += a3;
            a3 *= 2;
            if (t1 == 0)
                break;
        }
        if (a1 > m-1)
            a1 = m-1;
        a3 = 1;
        t1 = (1<<(n-1));
        t2 = 0;
        while (t2+a3 < p) {
            t2 += a3;
            a2 += t1;
            t1 /= 2;
            a3 *= 2;
        }
        if (a2 > m-1)
            a2 = m-1;
        cout << a1 << " " << a2 << endl;
    }
    return 0;
}
