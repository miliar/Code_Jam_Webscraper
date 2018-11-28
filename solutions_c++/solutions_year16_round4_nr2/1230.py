#include <iostream>
#include <stdio.h>
#include <cstring>
#include <iomanip>


using namespace std;

int n, k;
double a[20];
double bst;
bool used[20];

void try_cur() {
    double chance[20];
    for (int i = 1; i <= k; ++i)
        chance[i] = 0;
    chance[0] = 1;
    for (int i = 0; i < n; ++i) {
        if (used[i]) {
            double p = a[i];
            for (int j = k; j > 0; --j) {
                chance[j] = chance[j - 1] * p + chance[j] * (1 - p);
            }
            chance[0] = chance[0] * (1 - p);
        }
    }
    if (chance[k / 2] > bst)
        bst = chance[k / 2];
}

void gen(int v, int k) {
    if (v == n) {
        try_cur();
    }
    if (k > 0) {
        used[v] = true;
        gen(v + 1, k - 1);
    }
    if (n - v > k) {
        used[v] = false;
        gen(v + 1, k);
    }
}

void solve() {
    bst = 0;
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    gen(0, k);
    cout << fixed << setprecision(18) << bst << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "CASE #" << i << ": ";
        solve();
        //check(b, m);
    }
}
