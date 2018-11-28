#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cassert>
#include<climits>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<sstream>
#include<fstream>
#define debug puts("-----")
#define pi (acos(-1.0))
#define eps (1e-8)
#define inf (1<<30)
#define INF (1ll<<62)
using namespace std;
int A[5][5] =
{
    {0, 1, 2, 3, 4},
    {1, 1, 2, 3, 4},
    {2, 2, -1, 4, -3},
    {3, 3, -4, -1, 2},
    {4, 4, 3, -2, -1}
};
const int N = 10005;
int a[N], b[N];
int get(int x, int y)
{
    int t = A[abs(x)][abs(y)];
    if (x < 0) t *= -1;
    if (y < 0) t *= -1;
    return t;
}
int main ()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        string s;
        char str[N];
        int l, x, n;
        scanf("%d%d%s", &l, &x, str);
        s = str;
        for (int i = 1; i < x; i++) s += str;
        n = l * x;
        printf("Case #%d: ", ++cas);
        if (n < 3)
        {
            puts("NO");
            continue;
        }
        int q[200]={};
        q['i'] = 2, q['j'] = 3, q['k'] = 4;
        a[0] = q[s[0]];
        b[n - 1] = q[s[n - 1]];
        for (int i = 1; i < n; i++)
        {
            a[i] = get(a[i - 1], q[s[i]]);
            b[n - i - 1] = get(q[s[n - i - 1]], b[n - i]);
        }
        for (int i = 0; i < n - 2; i++)
            if (a[i] == 2)
            {
                for (int j = i + 2; j < n; j++)
                    if (b[j] == 4)
                    {
                        if (get(a[i], 3) == a[j - 1])
                        {
                            puts("YES");
                            goto gg;
                        }
                    }
            }
        puts("NO");
gg:
        ;
    }
    return 0;
}
