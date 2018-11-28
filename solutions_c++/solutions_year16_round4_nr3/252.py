#include <bits/stdc++.h>

using namespace std;

// 0 -> /
// 1 -> \

const int nmax = 109;

int what[nmax][nmax];
int where[nmax] , t[nmax] , p[nmax];
int test , T , n , m , i , j , ok;

int multime(int x)
{
    if (x == t[x]) return t[x];
    else return t[x] = multime(t[x]);
}

void unite(int u , int v)
{
    u = multime(u);
    v = multime(v);

    if (u == v) return;
    t[u] = v;
}

void check()
{
    for (i = 1 ; i <= 4 * n * m ; ++i)
    t[i] = i;

    for (i = 1 ; i <= n ; ++i)
    for (j = 1 ; j <= m ; ++j)
    {
        int p = 4 * (i - 1) * m + 4 * (j - 1);
        if (what[i][j] == 0)
        {
            unite(p + 1 , p + 2);
            unite(p + 3 , p + 4);
        }
        else
        {
            unite(p + 2 , p + 3);
            unite(p + 1 , p + 4);
        }
    }

    for (i = 2 ; i <= n ; ++i)
    for (j = 1 ; j <= m ; ++j)
    {
        int p1 = 4 * (i - 1) * m + 4 * (j - 1) + 1;
        int p2 = 4 * (i - 2) * m + 4 * (j - 1) + 3;

        unite(p1 , p2);
    }

    for (i = 1 ; i <= n ; ++i)
    for (j = 2 ; j <= m ; ++j)
    {
        int p1 = 4 * (i - 1) * m + 4 * (j - 2) + 4;
        int p2 = 4 * (i - 1) * m + 4 * (j - 1) + 2;

        unite(p1 , p2);
    }

    int u = 1;
    for (i = 1 ; i <= 2 * (n + m) ; i += 2)
    {
        int p1 = where[p[i]];
        int p2 = where[p[i + 1]];

        if (multime(p1) != multime(p2))
        {
            u = 0;
            break;
        }
    }

    if (u == 1)
    {
        ok = 1;
        for (i = 1 ; i <= n ; ++i , cout << '\n')
        for (j = 1 ; j <= m ; ++j)
        if (what[i][j] == 0) cout << '/';
        else cout << '\\';
    }
}

void bkt(int i , int j)
{
    if (ok) return;

    if (i == n + 1)
    {
        check();
        return;
    }

    what[i][j] = 1;
    if (j == m) bkt(i + 1 , 1);
    else bkt(i , j + 1);

    what[i][j] = 0;
    if (j == m) bkt(i + 1 , 1);
    else bkt(i , j + 1);
}

int main()
{
freopen("test.in" , "r" , stdin);
freopen("test.out" , "w" , stdout);

cin >> T;
for (test = 1 ; test <= T ; ++test)
{
    cin >> n >> m;
    memset(what , 0 , sizeof(what));
    memset(where , 0 , sizeof(where));
    memset(p , 0 , sizeof(p));

    for (i = 1 ; i <= 2 * (n + m) ; ++i)
    cin >> p[i];

    for (i = 1 ; i <= m ; ++i)
    where[i] = 4 * (i - 1) + 1;

    for (i = 1 ; i <= n ; ++i)
    where[i + m] = 4 * m * i;

    for (i = 1 ; i <= m ; ++i)
    where[n + m + m - i + 1] = 4 * (n - 1) * m + 4 * (i - 1) + 3;

    for (i = 1 ; i <= n ; ++i)
    where[n + n + m + m - i + 1] = (i - 1) * 4 * m + 2;

    //for (i = 1 ; i <= 2 * (n + m) ; ++i)
    //cerr << where[i] << " ";
    //cerr << '\n';

    cout << "Case #" << test << ":\n";

    ok = 0;
    bkt(1 , 1);
    if (ok == 0) cout << "IMPOSSIBLE\n";
}

return 0;
}
