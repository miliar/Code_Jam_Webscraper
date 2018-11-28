#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 1010;

int n;
int a[MAXN];
int f[MAXN][MAXN];

void preprocessing() {
    for (int mx_level = 1; mx_level < MAXN; mx_level++) {
        for (int level = 0; level <= mx_level; level++) {
            f[mx_level][level] = 0;
        }
        for (int level = mx_level + 1; level < MAXN; level++) {
            f[mx_level][level] = 1000000000;
            for (int a = 1; a < level; a++) {
                f[mx_level][level] = min(f[mx_level][level], f[mx_level][a] + f[mx_level][level - a] + 1);
            }
        }
    }
}

int solve() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int answer = 1000000000;
    for (int mx_level = 1; mx_level < MAXN; mx_level++) {
        int current_penalty = 0;
        for (int i = 0; i < n; i++) {
            current_penalty += f[mx_level][a[i] ];
        }
        answer = min(answer, current_penalty + mx_level);
    }
    return answer;
}

int main() {
    preprocessing();
    int t; cin >> t;
    for ( int i = 1; i <= t; i++ ) {
        cout << "Case #" << i << ": " << solve() << "\n";
        cerr << "Case #" << i << " is done!\n";
    }
    return 0;
}