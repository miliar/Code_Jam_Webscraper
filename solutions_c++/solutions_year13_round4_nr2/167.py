#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

int n;
long long p;

long long getans2()
{
    long long tot = (1LL << n);
    long long low = 0, high = tot - 1;
    long long ans = -1;
    while (low <= high) {
        long long mid = low + high >> 1;
        long long worse_than = tot - mid - 1;
        int cnt = 0;
        while (worse_than > 0) {
            cnt++;
            worse_than = (worse_than - 1) / 2;
        }
        if ((1LL << n - cnt) <= p) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

long long getans1()
{
    long long tot = (1LL << n);
    long long low = 0, high = tot - 1;
    long long ans = -1;
    while (low <= high) {
        long long mid = low + high >> 1;
        long long better_than = mid; 
        int cnt = 0;
        while (better_than > 0) {
            cnt++;
            better_than = (better_than - 1) / 2;
        }
        if (tot - (1LL << n - cnt) + 1 <= p) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

void solve() 
{
    cin >> n >> p;

    cout << getans1() << " " << getans2() << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; ++_) {
        printf("Case #%d: ", _);
        solve();
    }
}

