#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int N = 20;
int mine[N * N];
bool a[N][N];
bool seen[N][N];
int n, m;

const int DI[] = { -1, -1, -1, 0, 0, 1, 1, 1 } ;
const int DJ[] = { -1, 0, 1, -1, 1, -1, 0, 1 } ;

void dfs(int i, int j)
{
    if(i < 0 || j < 0 || i >= n || j >= m) return;
    if(seen[i][j]) return;
    if(a[i][j]) return;

    seen[i][j] = true;

    for(int d = 0; d < 8; d++)
    {
        int ii = i + DI[d], jj = j + DJ[d];
        if(ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
        if(a[ii][jj]) return;
    }

    for(int d = 0; d < 8; d++) dfs(i + DI[d], j + DJ[d]);
}

bool ok(int si, int sj)
{
    if(a[si][sj]) return false;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            seen[i][j] = false;

    dfs(si, sj);

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            if(!seen[i][j] && !a[i][j]) return false;
    return true;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int test;
    scanf("%i", &test);
    //for(int i = 0; i < test; i++) fprintf(stderr, "="); fprintf(stderr, "\n");
    for(int t = 1; t <= test; t++)
    {
        int x;
        scanf("%i %i %i", &n, &m, &x);

        printf("Case #%i:\n", t);

        int area = n * m;
        //printf("A = %i X = %i\n", area, x);
        for(int i = 0; i < area; i++)
            mine[i] = (area - 1 - i) < x ? 1 : 0;
       // for(int i = 0; i < area; i++) printf("%c", mine[i] ? 'C' : 'a');

        bool done = false;

        do
        {
            for(int i = 0; i < n; i++)
                for(int j = 0; j < m; j++)
                    a[i][j] = mine[i * m + j] > 0;

            for(int si = 0; si < n; si++)
                for(int sj = 0; sj < m && !done; sj++)
                    if(ok(si, sj))
                    {
                        done = true;
                        for(int i = 0; i < n; i++)
                            for(int j = 0; j <= m; j++)
                                printf("%c", j == m ? '\n' : (i == si && j == sj) ? 'c' : a[i][j] ? '*' : '.');
                    }
        } while(!done && next_permutation(mine, mine + area)) ;

        if(!done) printf("Impossible\n");
        fprintf(stderr, "-");
    }
    return 0;
}
