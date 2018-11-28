#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <set>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = (int)1e7;

bool is_pal(ll x) {
    string s = "";
    if (x == 0) return 1;

    while (x != 0) {
        s += char(x % 10 + '0');
        x /= 10;
    }

    forn(i, s.length() / 2)
        if (s[s.length() - i - 1] != s[i])
            return 0;

    return 1;
}

int k[MAXN];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    k[0] = 0;
    forab(i, 1, MAXN)
        if (is_pal(i) && is_pal((ll)i * i))
            k[i] = k[i - 1] + 1;
        else
            k[i] = k[i - 1];

    int T;
    scanf("%d", &T);
    forn(t, T) {
        printf("Case #%d: ", t + 1);

        ll a, b;
        cin >> a >> b;
        ll l = (ll)(sqrt(a * 1.0)), r = (ll)(sqrt(b * 1.0));
        while ((l + 1) * (l + 1) < a) l++;
        while (l * l >= a) l--;
        while (r * r > b) r--;
        while ((r + 1) * (r + 1) <= b) r++;
        printf("%d\n", k[r] - k[l]);
    }
    return 0;
}
