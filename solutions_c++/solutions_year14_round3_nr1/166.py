#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define EPS 1.0e-6
#define INF 10000000

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    long long p, q, gcd;
    bool poss;
    int resp;

    scanf("%d", &T);
    for(int ncaso=1; ncaso<=T; ncaso++)
    {
        scanf("%lld/%lld", &p, &q);
        gcd = __gcd(p,q);
        p /= gcd; q /= gcd;

        poss = false;
        for(int i=0; i<=40; i++)
        {
            if ((1LL << i) == q)
            {
                poss = true;
                break;
            }
        }

        resp = -1;
        for(int i=0; i<=40; i++)
        {
            if (p >= q) {resp = i; break;}
            q /= 2;
        }

        if (resp == -1 || !poss) printf("Case #%d: impossible\n", ncaso);
        else printf("Case #%d: %d\n", ncaso, resp);
    }

    return 0;
}
