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
#define MAXN 1005

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int v[MAXN];
int trocas;
void Merge(int ini, int fim)
{
    static int aux[MAXN];
    int i, meio=(ini+fim)/2, e, d;

    if(ini < fim)
    {
        Merge(ini, meio);
        Merge(meio+1, fim);

        for(i=ini; i<=fim; i++)
            aux[i] = v[i];

        i = ini;
        e = ini;
        d = meio+1;

        while(e<=meio && d<=fim)
        {
            if(aux[e] <= aux[d])
                v[i++] = aux[e++];
            else
            {
                v[i++] = aux[d++];
                trocas += meio-e+1;
            }
        }

        while(e <= meio)
            v[i++] = aux[e++];

        while(d <= fim)
            v[i++] = aux[d++];
    }
}

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);

    int T;
    int n, a[MAXN], s[MAXN], maior;
    int resp;
    bool check;

    scanf("%d", &T);
    for(int ncaso=1; ncaso<=T; ncaso++)
    {
        scanf("%d", &n);
        FOR(i,0,n) scanf("%d", &a[i]), s[i] = a[i];

        resp = INF;
        sort(a,a+n); maior = a[n-1];
        do
        {
            //printf("%d %d %d\n", a[0], a[1], a[2]); system("pause");

            check = true;
            int I = 0;
            for(; a[I]!=maior; I++)
                if (a[I] > a[I+1])
                    check = false;

            if (!check) continue;

            for(I=I+1; I<n; I++)
                if (a[I] > a[I-1])
                    check = false;

            if (!check) continue;

            map<int, int> mapa;
            FOR(i,0,n) mapa[ a[i] ] = i;
            FOR(i,0,n) v[i] = mapa[ s[i] ];

            trocas = 0;
            Merge(0,n-1);

            /*FOR(i,0,n) printf("%d ", a[i]); putchar(10);
            FOR(i,0,n) printf("%d ", v[i]); putchar(10);
            printf("%d\n\n", trocas);*/

            resp = min(resp, trocas);
        } while(next_permutation(a,a+n));

        printf("Case #%d: %d\n", ncaso, resp);
    }

    return 0;
}
