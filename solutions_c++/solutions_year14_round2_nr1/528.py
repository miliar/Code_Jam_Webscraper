#include <iostream>
#include <cstdio>

using namespace std;

struct block { char c; int n; } ;
void make_block(char s[], block a[], int &n)
{
    n = 0;
    for(int i = 0; s[i]; i++)
        if(!n || a[n - 1].c != s[i])
        {
            a[n].c = s[i]; a[n].n = 1;
            n++;
        }
        else a[n - 1].n++;
}

const int N = 200;
block b[N][N];
char s[N];

int abs(int x) { return x < 0 ? -x : x; }

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int t;
    scanf("%i", &t);
    for(int te = 1; te <= t; te++)
    {
        int n;
        scanf("%i", &n);

        int m;
        bool cando = true;
        for(int i = 0; i < n; i++)
        {
            scanf(" %s", &s);
            int k;
            make_block(s, b[i], k);
            if(i && k != m) cando = false;
            m = k;
        }

        int res = 0;
        if(cando)
        {
            for(int i = 0; i < m; i++)
            {
                for(int j = 0; j < n; j++)
                    if(b[j][i].c != b[0][i].c) cando = false;

                int best = 1 << 30;
                for(int to = 1; to <= 100; to++)
                {
                    int x = 0;
                    for(int j = 0; j < n; j++)
                        x += abs(b[j][i].n - to);
                    best = min(best, x);
                }

                res += best;
            }
        }

        printf("Case #%i: ", te);
        if(cando && res != -1) printf("%i\n", res);
        else printf("Fegla won\n");
    }
    return 0;
}
