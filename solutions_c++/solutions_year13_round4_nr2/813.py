#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#define rep(i, n) for(int i = 0; i < (n); i++)
#define rev(i, n) for(int i = (n) - 1; i >= 0; --i)
using namespace std;

void bug() { cout << " " << endl; }
template<class T> void bug(T a) { cout << a << "  "; }
template<class T> void bug(T* a, int n) {rep(i, n) bug(a[i]);}

int check(long long x, long long n, long long p) {
    long long total = (1 << n);
    long long left = x, right = total - 1 - left;
    long long rank = 0;
    for(int i = n - 1; i >= 0; --i) {
        if(left & 1) {
            total /= 2;
            rank += total;
            left >>= 1;
            right = total - 1 - left;
        }
        else if(left == 0)
            break;
        else {
            total /= 2;
            left = (left - 2) / 2;
            rank += total;
            right = total - 1 - left;
        }
    }
    return rank < p;
}

long long run1(long long n, long long p) {
    long long l = 0, r = 1 << n;
    while(l + 1 < r) {
        long long mid = (l + r) >> 1;
        if(check(mid, n, p)) l = mid;
        else r = mid;
    }
    return l;
}

long long check2(long long x, long long n, long long p) {
    long long total = (1 << n);
    long long left = x, right = total - 1 - left;
    long long rank = 0;
    for(int i = n - 1; i >= 0; --i) {
        if(right == 0) { rank = total - 1; }
        else if(right & 1) {
            total /= 2;
            right = right / 2;
            left = total - 1 - right;
        }
        else {
            total /= 2;
            right = (right - 2) / 2;
            left = total - 1 - right;
        }
    }
    return rank < p;
}

long long run2(long long n, long long p) {
    long long l = 0, r = 1 << n;
    while(l + 1 < r) {
        long long mid = (l + r) >> 1;
        if(check2(mid, n, p)) l = mid;
        else r = mid;
    }
    return l;
}

int main() {
    int t;
    cin >> t;
    rep(i, t) {
        long long n, p;
        cin >> n >> p;
        printf("Case #%d: %lld %lld\n", i + 1, run1(n, p), run2(n, p));
    }
    return 0;
}
