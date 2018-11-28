#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <stdlib.h>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
#include <ctime>
#include <queue>
#include <deque>
#include <memory.h>
#include <complex>
#include <numeric>

#define mp make_pair
#define pb push_back
#define fi first
#define se second

#define INF (1000000000)
#define LINF (1000000000000000000ll)
#define EPS (1e-9)

#define MOD 1000000007

#define NAME "test"
#ifndef NAME
    #error Write problem name!
#endif

using namespace std;

typedef long long li;
typedef unsigned long long uli;

li gcd(li x, li y){
    if (y == 0)
        return x;
    else
        return gcd(y, x % y);
}

li lcm(li x, li y){
    return x / gcd(x, y) * y;
}

li binpow(li a, li p){
    if (!p)
        return 1;
    li g = binpow(a, p >> 1);
    if (p % 2 == 0)
        return (g * g) % MOD;
    else
        return (((g * g) % MOD) * a) % MOD;
}

li rev(li n){
    return binpow(n, (li)MOD - 2LL);
}

void solve(int test_number);

int main() {
#ifdef _GEANY
    assert(freopen(NAME ".in", "r", stdin));
    assert(freopen(NAME ".out", "w", stdout));
#endif
    cout.setf(ios::fixed);
    cout.precision(20);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; ++i)
        solve(i + 1);
}

int a[5][5], b[5][5];

void solve(int test_number) {
    int ra, rb;
    cin >> ra;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            cin >> a[i][j];
    ra--;
    cin >> rb;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            cin >> b[i][j];
    rb--;
    set<int> q;
    for (int i = 0; i < 4; i++){
        q.insert(a[ra][i]);
    }
    int ans = -1;
    for (int i = 0; i < 4; i++)
        if (q.count(b[rb][i]) != 0) {
            if (ans == -1)
                ans = b[rb][i];
            else
                ans = -2;
        }
    cout << "Case #" << test_number << ": ";
    if (ans == -2)
        cout << "Bad magician!\n";
    else if (ans == -1)
        cout << "Volunteer cheated!\n";
    else
        cout << ans << endl;
}

