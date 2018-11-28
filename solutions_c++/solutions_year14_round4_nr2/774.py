#include <iostream>
#include <cmath>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int DEBUG = 1;

int n;
int t;
int c[1005];
int a[1005];
int b[1005];
int sz = 0;
int q[1005];

int solve() {
    int ret = 0;
    for (int i = 0; i < sz; ++i)
        for (int j = 0; j < sz - 1; ++j)
            if (q[j] > q[j + 1]) {
                swap(q[j], q[j + 1]);
                ++ret;
            }
    return ret;
}

int main()
{
    if (DEBUG) {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
    cin >> t;
    int number = 0;
    while (t--) {
        cin >> n;
        ++number;
        for (int i = 0; i < n; ++i) cin >> a[i];
        cout << "Case #" << number << ": ";
        int ans = 1000000000;
        for (int i = 0; i < n; ++i) b[i] = a[i];
        sort(b, b + n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j)
                if (a[i] == b[j]) {
                    a[i] = j;
                    break;
                }
        }
        ans = 0;

        int pL = 0, pR = n - 1;
        for (int i = 0; i < n - 1; ++i) {
            int e = -1;
            for (int j = 0; j < n; ++j)
                if (a[j] == i) e = j;
            if (abs(e - pL) > abs(e - pR)) {
                while (e != pR) {
                    swap(a[e], a[e+1]);
                    e++;
                    ans++;
                }

                pR--;
            }
            else {
                while (e != pL) {
                    swap(a[e], a[e-1]);
                    e--;
                    ans++;
                }
                pL++;
            }
        }
        cout << ans << endl;
    }
    return 0;
};

