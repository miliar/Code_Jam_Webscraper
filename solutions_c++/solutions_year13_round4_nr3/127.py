#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <set>
#include <vector>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int a[2010];
int b[2010];
int x[2010];

int pos[2010];

int n;

bool gen(int p) {
    if (p == n + 1) {
        forn(i, n)
            printf("%d ", x[i]);
        printf("\n");
        return 1;
    }
    int cur_a, cur_b;
    forn(i, n)
        if (x[i] == n + 1) {
            cur_a = 1, cur_b = 1;
            forab(j, 1, p)
                if (pos[j] < i)
                    cur_a = max(a[pos[j]] + 1, cur_a);
                else
                    cur_b = max(b[pos[j]] + 1, cur_b);
            if (a[i] != cur_a || b[i] != cur_b)
                continue;
            pos[p] = i;
            x[i] = p;
            if (gen(p + 1))
                return 1;
            x[i] = n + 1;
        }
    return 0;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    forn(t, T) {
        printf("Case #%d: ", t + 1);
        cin >> n;
        forn(i, n)
            cin >> a[i];
        forn(i, n)
            cin >> b[i];
        forn(i, n)
            x[i] = n + 1;
        if (!gen(1)) {
            cerr << "fail\n";
            return 0;
        }
    }
    return 0;
}
