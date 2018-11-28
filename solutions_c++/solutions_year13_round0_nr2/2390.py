#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int T;

int n, m;
int a[110][110];
int mx[110];
int my[110];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    forn(t, T) {
        cin >> n >> m;
        forn(i, n)
            forn(j, m)
                cin >> a[i][j];

        forn(i, n) {
            mx[i] = a[i][0];
            forn(j, m)
                mx[i] = max(mx[i], a[i][j]);
        }

        forn(j, m) {
            my[j] = a[0][j];
            forn(i, n)
                my[j] = max(my[j], a[i][j]);
        }

        string ans = "YES";

        forn(i, n)
            forn(j, m)
                if (a[i][j] != mx[i] && a[i][j] != my[j])
                    ans = "NO";

        printf("Case #%d: ", t + 1);
        cout << ans << '\n';

    }
    return 0;
}
