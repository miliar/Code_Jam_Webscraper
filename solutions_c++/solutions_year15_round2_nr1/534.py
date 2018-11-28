#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long ll;

ll rev(ll a) {
    ll b = 0;
    while (a != 0) {
        b = b * 10 + a%10;
        a /= 10;
    }
    return b;
}


const int maxn = 2000000;
int d[maxn];

int Len(ll n) {
    int res = 0;
    while (n != 0) {
        ++res;
        n /= 10;
    }
    return res;
}

ll Do3(ll n) {
    ll res = 1;
    while (n != 1) {
        int len = Len(n);
        int cnt = len/2;
        ll cur = n;
        for (int i = 0; i < cnt; ++i) cur /= 10;
        for (int i = 0; i < cnt; ++i) cur *= 10;
        cur += 1;
        if (cur > n) {
            --n;
            ++res;
        } else {
            res += n - cur;
            n = rev(cur);
            if (rev(cur) != cur) ++res;
            --n;
            ++res;
        }
    }
   
    return res;
}
int p[maxn];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ll n;
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        cin >> n;
        /*d[1] = 1;
        for (int i = 1; i < n; ++i) {
            
            if (d[i + 1] > d[i ] + 1) p[i + 1] = i;
            d[i + 1] = min(d[i + 1], d[i] + 1);
            int rr = rev(i);
            if (d[rr] > d[i] + 1) p[rr] = i;
            d[rr] = min(d[rr], d[i] + 1);

            assert(d[i] == Do3(i));
        } */
        cout << "Case #"<<test<<": " << Do3(n) << "\n";
    }                 
}