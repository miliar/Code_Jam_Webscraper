#include <iostream>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>


using namespace std;

#define ll long long
#define y1 _dfdfdfd


const int maxn = 1 << 18;
const int inf = 1000000007;
const int mod = 1000000007;

int n;
int a[maxn];

int b[maxn], posa[maxn], posb[maxn];
int slowsolve() {
    for (int i = 0; i < n; i++) b[i] = a[i];
    for (int i = 0; i < n; i++) posa[a[i]] = i;
    
    int res = 1e9;
    sort(b, b + n);
    do {
        for (int i = 0; i < n; i++) posb[b[i]] = i;
        int ans = 0;
        for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) ans += (posa[i] < posa[j]) != (posb[i] < posb[j]);
        int cur = n > 1 && b[1] < b[0];
        for (int i = 1; i + 1 < n; i++) cur += (b[i] < b[i + 1]) != (b[i - 1] < b[i]);
        if (cur <= 1 && res > ans) {
            res = min(res, ans);
        }
    } while (next_permutation(b, b + n));
    return res;
}
 
int fastsolve() {
    /*for (int i = 0; i < n; i++) b[i] = a[i];
    int ps = -1;
    for (int i = 0; i < n; i++) {
        if (b[i] == n - 1) {
            ps = i;
            while (i) {
                swap(b[i], b[i - 1]);
                i--;
            }
            break;
        }
    }
    
    int cntl = 0;
    int cntr = 0;
    for (int i = 1; i < n; i++) for (int j = i + 1; j < n; j++) if (b[i] < b[j]) cntr++;
    
    int res = 1e9;
    for (int i = 0; i < n; i++) {
        res = min(res, cntl + cntr + abs(i - ps));
        if (i == n - 1) break;
        swap(b[i], b[i + 1]);
        for (int j = 0; j < i; j++) if (b[j] > b[i]) cntl++;
        for (int j = i + 2; j < n; j++) if (b[j] > b[i]) cntr--;
    }
    return res;*/
    for (int i = 0; i < n; i++) b[i] = a[i];
    int ans = 0;
    int l = 0, r = n - 1;
    for (int it = 0; it < n; it++) {
        for (int i = l; i <= r; i++) {
            if (b[i] == it) {
                if (i - l <= r - i) {
                    ans += i - l;
                    while (i > l) {
                        swap(b[i], b[i - 1]);
                        i--;
                    }
                    l++;
                } else {
                    ans += r - i;
                    while (i < r) {
                        swap(b[i], b[i + 1]);
                        i++;
                    }
                    r--;
                }
                break;
            }
        }
    }
    return ans;
}
 
void gen() {
    n = rand() % 8 + 1;
    for (int i = 0; i < n; i++) a[i] = rand() % (int)1e9;
}
 
void work() {
    for (int i = 0; i < n; i++) b[i] = a[i];
    sort(b, b + n);
    for (int i = 0; i < n; i++) a[i] = lower_bound(b, b + n, a[i]) - b;
}
 
void stress(bool f) {
    if (!f) return;
    for (int it = 0; it < 1e9; it++) {
        gen();
        work();
        int res1 = slowsolve();
        int res2 = fastsolve();
        if (res1 != res2) {
            cout << res1 << " " << res2 << endl;
            cout << n << endl;
            for (int i = 0; i < n; i++) cout << a[i] << " \n"[i + 1 == n];
            slowsolve();
            fastsolve();
            break;
        }
        cerr << it << endl;
    }
    exit(0);
} 

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    stress(0);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        cin >> n;
        for (int i = 0; i < n; i++) cin >> a[i];
        work();
        cout << fastsolve() << endl;
        cerr << test << endl;
    }

	return 0;
}
