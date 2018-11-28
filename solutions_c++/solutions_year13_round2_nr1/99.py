#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

ll a;
int n;
ll x[110];

int ans;

void upd(int i) {
    int cur = i;
    ll sum = a;
    forn(j, n - i) {
        while (sum <= x[j]) {
            if (sum <= 1)
                return;
            cur++;
            sum += sum - 1;
        }
        sum += x[j];
    }
    ans = min(ans, cur);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(t, T) {
        printf("Case #%d: ", t + 1);
        cin >> a >> n;
        forn(i, n)
            cin >> x[i];

        ans = 100500;
        sort(x, x + n);
        forn(i, n + 1)
            upd(i);
        printf("%d\n", ans);
    }
    return 0;
}
