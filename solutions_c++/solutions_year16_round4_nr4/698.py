//writed by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
using namespace std;
typedef long long LL;
typedef pair <int, int> P;
const int NUM = 100010;
int n, b, m, ans, c[5][5], d[5];
char buf[10][10];
void print_bit(int x)
{
    for(int i = 0; i < m; ++i) printf("%c", x & (1 << i) ? '1' : '0'); puts("");
}
bool dfs(int i, int mask)
{
    if(i == n) return true;
    bool flag = false;
    for(int j = 0; j < n; ++j)
    {
        if(c[d[i]][j] && !(mask & (1 << j)))
        {
            flag = true;
            if(!dfs(i + 1, mask | (1 << j)))
                return false;
        }
    }
    return flag;
}
bool check(int mask)
{
    for(int i = 0; i < n; ++i)
    {
        d[i] = i;
        for(int j = 0; j < n; ++j)
        {
            if(mask & (1 << (i * n + j)))
                c[i][j] = 1;
            else
                c[i][j] = 0;
        }
    }
    do
    {
        if(!dfs(0, 0)) return false;
    }
    while(next_permutation(d, d + n));
    return true;
}
int main()
{
#ifdef ACM_TEST
//    freopen("in.txt", "r", stdin);
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
#endif
    int T; scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        scanf("%d", &n);
        m = n * n;
        b = 0;
        for(int i = 0; i < n; ++i)
        {
            scanf("%s", buf[i]);
            for(int j = 0; j < n; ++j)
            {
                if(buf[i][j] == '1')
                    b |= (1 << (i * n + j));
            }
        }
//        print_bit(b);
        ans = m;
        for(int i = (1 << m) - 1; i >= 0; --i)
        {
            if((i & b) == b)
            {
                if(check(i))
                {
//                  print_bit(i);
                    int res = 0;
                    for(int j = 0; j < m; ++j)
                        if((i & (1 << j)) ^ (b & (1 << j)))
                            ++res;
                    ans = min(ans, res);
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
