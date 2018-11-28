#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cctype>

using namespace std;

#define MAXN 128
#define EPS (1e-10)

typedef long long ll;

bool isPalindrome(ll n) {
    char s[MAXN];

    sprintf (s, "%lld", n);
    int tam = strlen(s);

    for (int i = 0; i <= tam / 2; ++i) {
        if (s[i] != s[tam-i-1]) return false;
    }

    return true;
}

int main () {
    int casos;
    scanf ("%d", &casos);

    for (int caso = 1; caso <= casos; ++caso) {
        ll a, b;
        scanf ("%lld %lld", &a, &b);

        ll ans = 0;
        if (a > b) swap(a, b);
        for (ll i = (ll) ceil(sqrt(a) - EPS); i*i <= b; ++i) {
            if (!isPalindrome(i)) continue;
            if (isPalindrome(i*i)) ++ans;
        }

        printf ("Case #%d: ", caso);
        printf ("%lld\n", ans);
    }

    return 0;
}

