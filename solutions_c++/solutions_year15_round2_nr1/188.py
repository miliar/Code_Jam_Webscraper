#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

const int MAXN = 1000000;

int dp[MAXN + 1];

long long reverse(long long n) {
    long long rev = 0;
    while (n > 0) {
        rev = n % 10 + rev * 10;
        n /= 10;
    }
    return rev;
}

int digits(long long n) {
    int cnt = 0;
    while (n > 0) {
        cnt++;
        n /= 10;
    }
    return cnt;
}

long long power(int n) {
    long long p = 10;
    for (int i = 0; i < n; i++) {
        p *= 10;
    }
    return p;
}

long long getdp(long long n) {
    if (n <= 10) {
        return n;
    }
    long long num = power((digits(n) - 1) / 2);
    long long m = (n / num) * num + 1;
    if (m > n) {
        return getdp(n - 1) + 1;
    }
    else if (reverse(m) == m) {
        return getdp(m - 1) + (n - m) + 1;
    }
    return getdp(reverse(m)) + (n - m) + 1;
}

void precalc() {
    dp[0] = 0;
    for (int i = 1; i <= MAXN; i++) {
        dp[i] = i;
    }
    for (int i = 0; i < MAXN; i++) {
        dp[i + 1] = min(dp[i + 1], dp[i] + 1);
        long long rev = reverse(i);
        dp[rev] = min(dp[rev], dp[i] + 1);
    }
    for (int i = 1; i <= MAXN; i++) {
        long long dpi = getdp(i);
        if (dp[i] != dpi) {
            cout << i << " " << dpi << " " << dp[i] << endl;
        }
    }
}

void solve() {
    long long n;
    cin >> n;
    cout << getdp(n);
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("A-large.in-2.txt", "rt", stdin);
//        freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
//    precalc();
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
}
