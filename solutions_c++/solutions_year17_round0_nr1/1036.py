#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795

#define fill(x, v)  fillchar(x, v, sizeof(x))
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;


#define MAXN 100500

int  tc;
char s[MAXN];
int  k, ans;
bool ok;

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt = 1; tt <= tc; ++tt) {
        scanf("%s%i", s, &k);
        ans = 0;
        for(int i = 0, n = strlen(s); i + k <= n; ++i)  if (s[i] == '-') {
            for(int j = 0; j < k; ++j) if (s[i + j] == '+') s[i + j] = '-'; else s[i + j] = '+';
            ans++;
        }

        ok = true;
        for(int i = 0; i < strlen(s); ++i) ok = ok && s[i] == '+';

        printf("Case #%i: ", tt);
        if (ok)
            printf("%i\n", ans);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}