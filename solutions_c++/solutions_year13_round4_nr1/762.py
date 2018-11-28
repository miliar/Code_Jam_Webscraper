#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long lld;

struct travel{
    lld e;
    lld o;
    lld p;
};

travel a[2013];
lld s[2013 * 6];
lld p[2013 * 6];
int n, m;
const lld P = 1000002013;

lld normal()
{
    lld ret = 0;
    for (int i=0; i<m; ++i) {
        lld r = (a[i].o-a[i].e);
        ret += (r * n % P- r * (r - 1) / 2 % P) * (a[i].p % P)%P;
        ret %= P;
    }
    return ret;
}

lld cheap()
{
    for (int i=0; i<m; ++i) {
        s[i] = a[i].o;
        s[m+i] = a[i].e;
        s[m*2+i] = a[i].e - 1;
        s[m*3+i] = a[i].o - 1;
        s[m*4+i] = a[i].o + 1;
        s[m*5+i] = a[i].e + 1;
    }
    sort(s,s + m*6);
    s[m*6] = -1;
    int cnt = 0;
    for (int i=0; i<6*m; ++i) {
        if (s[i] == s[i+1]) continue;
        s[cnt] = s[i];
        ++cnt;
    }
    s[cnt] = 1100000000;
    ++cnt;

    for (int i=0; i<m; ++i) {
        for (int j=0; j<cnt; ++j) {
            if (a[i].e <= s[j] && a[i].o > s[j]) {
                p[j] += a[i].p;
            }
        }
    }
    bool allzero = false;
    int start = -1;
    lld ret = 0;
    lld min = 1100000000;
    while (!allzero) {
        allzero = true;
        for (int j=0; j<cnt; ++j) {
            if (p[j] != 0) {
                if (start == -1) {
                    start = j;
                    min = p[j];
                }
                if (p[j] < min) {
                    min = p[j];
                }
                allzero = false;
            } else if (j && p[j-1] != 0) {
                lld r = s[j] - s[start];
                ret += (r * n % P - r * (r - 1) / 2 % P) * (min % P)%P;
                ret %= P;
                for (int k=start; k<j; ++k) {
                    p[k] -= min;
                }
                min = 1100000000;
                start = -1;
            }
        }
        if (p[cnt - 1] != 0) {
            fprintf(stderr, "EEEE\n");
        }
    }
    return ret;
}

int main()
{
    //
    int T = 0;
    cin >> T;
    for (int t=1; t<T+1; ++t) {
        memset(a, sizeof(a), 0);
        memset(s, sizeof(s), 0);
        memset(p, sizeof(p), 0);
        cin >> n >> m;
        for (int i=0; i<m; ++i) {
            cin >> a[i].e >> a[i].o >> a[i].p;
        }
        lld ans = normal() - cheap();
        ans %= P;
        ans += P;
        ans %= P;
        printf("Case #%d: %lld\n", t, ans);
    }

    //
    return 0;
}

