#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const int NMAX = 105;
const int HMAX = 205;
const int SMAX = 1005;

int d[NMAX][SMAX][HMAX][2];

int n, p, q;
int h[NMAX], g[NMAX];

void solve(int test)
{
    printf("Case #%d: ", test);

    cerr << test << endl;

    scanf("%d %d %d", &p, &q, &n);

    forn(i, n) 
    {
        scanf("%d %d", &h[i], &g[i]);
    }

    memset(d, -1, sizeof(d));

    d[0][1][h[0]][0] = 0;
    h[n] = 0;

    int ans = 0;

    forn(i, n)
    {
        for (int a = h[i]; a >= 1; a--)
        {
            forn(j, SMAX)
            {
                forn(t, 2)
                {
                    if (d[i][j][a][t] == -1) continue;

                    if (t == 0)
                    {
                        if (j > 0)
                        {
                            if (a <= p)
                            {
                                d[i + 1][j - 1][h[i + 1]][0] = max(d[i + 1][j - 1][h[i + 1]][0], d[i][j][a][t] + g[i]);
                                ans = max(ans, d[i][j][a][t] + g[i]);
                            }
                            else
                            {
                                d[i][j - 1][a - p][0] = max(d[i][j - 1][a - p][0], d[i][j][a][t]);
                            }
                        }
                        d[i][j][a][1] = max(d[i][j][a][1], d[i][j][a][t]);   
                    }
                    else // t == 1
                    {
                        if (a <= q)
                        {
                            d[i + 1][j + 1][h[i + 1]][0] = max(d[i + 1][j + 1][h[i + 1]][0], d[i][j][a][t]);
                        }
                        else
                        {   
                            d[i][j + 1][a - q][0] = max(d[i][j + 1][a - q][0], d[i][j][a][t]);
                        }
                    }
                }
            }
        }            
    }
    cout << ans << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
