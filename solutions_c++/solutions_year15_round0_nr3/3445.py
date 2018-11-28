/*
ID: Loeabc123456@gmail.com
PROG:
LANG: C++
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;
int A[5][5] =
{
    {0, 1, 2, 3, 4},
    {1, 1, 2, 3, 4},
    {2, 2, -1, 4, -3},
    {3, 3, -4, -1, 2},
    {4, 4, 3, -2, -1}
};
map<char, int> M;
const int N = 10000 + 10;
int l, x, n;
char str[N];
string s;
int aa[N], bb[N];
int get(int x, int y)
{
    int xx = fabs(x), yy = fabs(y);
    int t = A[xx][yy];
    if (x < 0) t *= -1;
    if (y < 0) t *= -1;
    return t;
}
void work()
{
    M['i'] = 2, M['j'] = 3, M['k'] = 4;
    aa[0] = M[s[0]];
    bb[n - 1] = M[s[n - 1]];
    for (int i = 1; i < n; i++)
    {
        aa[i] = get(aa[i - 1], M[s[i]]);
        bb[n - i - 1] = get(M[s[n - i - 1]], bb[n - i]);
    }
}
int main ()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ii = 1; ii <= T; ii++)
    {
        scanf("%d%d%s", &l, &x, str);
        s = str;
        for (int i = 1; i < x; i++) s += str;
        n = l * x;
        printf("Case #%d: ", ii);
        if (n < 3)
        {
            puts("NO");
            continue;
        }
        work();
        bool flag = 0;
        for (int i = 0; i < n - 2; i++) if (aa[i] == 2)
            {
                for (int j = i + 2; j < n; j++) if (bb[j] == 4)
                    {
                        if (get(aa[i], 3) == aa[j - 1])
                        {
                            puts("YES");
                            flag = 1;
                            break;
                        }
                    }
                if (flag) break;
            }
        if (!flag) printf("NO\n");
    }
    return 0;
}
