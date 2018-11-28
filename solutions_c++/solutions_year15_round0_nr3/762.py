#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define push_back pb
#define make_pair mp

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define MAXN 10005000

ll   x;
int  n, tc;
char s[MAXN];
int  a[MAXN];
bool ok;
int  p1, p2;
int  res;

int f[4][4] = {
  {1, 2, 3, 4},
  {2, -1, 4, -3},
  {3, -4, -1, 2},
  {4, 3, -2, -1}
};

int mul(int x, int y) {
    int sign = 1;
    if (x < 0) {
        sign = -sign;
        x = -x;
    }
    if (y < 0) {
        sign = -sign;
        y = -y;
    }
    

    return f[x - 1][y - 1]*sign;
}

int power(int x, ll k) {
    int res = 1;
    while (k > 0) {
        if (k % 2 == 1) res = mul(res, x);
        k = k / 2;
        x = mul(x, x);
    }
    return res;
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        cin >> n >> x;
        scanf("%s", s);
        res = 1;
        for(int i=0; i<n; ++i) {
            a[i] = 1;
            if (s[i] == 'i') a[i] = 2;
            if (s[i] == 'j') a[i] = 3;
            if (s[i] == 'k') a[i] = 4;
            res = mul(res, a[i]);
        }

        res = power(res, x);
        ok = false;
        if (res == -1) {
            for(int i=n; i<n*10; ++i) a[i] = a[i - n];
            p1 = p2 = -1;

            res = 1;
            for(int i=0; i<n*10; ++i) {
                res = mul(res, a[i]);
                if (res == 2) {
                    p1 = i + 1;
                    break;
                }
            }

            res = 1;
            for(int i=n*10 - 1; i>=0; --i) {
                res = mul(a[i], res);
                if (res == 4) {
                    p2 = n*10 - i;
                    break;
                }
            }
            if (p1 > 0 && p2 > 0 && p1 + p2 < n*x) ok = true;
        }

        printf("Case #%i: ", tt);
        if (ok) printf("YES\n"); else printf("NO\n"); 
    }
    return 0;
}