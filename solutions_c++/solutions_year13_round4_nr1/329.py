
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

#define P 1000002013


int n, m;

struct node{
    int pos, num;
    int t;
}a[2100];

long long ans1, ans2;
int cnt = 0;

bool cmp(node a, node b)
{
    if (a.pos == b.pos) return a.t > b.t;
    return a.pos < b.pos;
}

int pos[10000], num[10000];
int tot;


int main()
{
    freopen("in.txt","r", stdin);
    int T, ca = 0;
    scanf("%d", &T);
    while (T--)
    {
       ans1 = 0;
       ans2 = 0;
       cnt = 0;
       scanf("%d%d", &n, &m);
       for (int i = 1; i <= m; i++)
       {
           int x, y, z;
           scanf("%d%d%d", &x, &y, &z);
           long long k = y - x, temp;
           temp = ((long long)n * 2 - k + 1) / 2 * k % P;
           temp = temp * (long long)z % P;
           ans1 += temp;
           ans1 %= P;
           a[++cnt].pos = x;
           a[cnt].num = z;
           a[cnt].t = 1;
           a[++cnt].pos = y;
           a[cnt].num = z;
           a[cnt].t = -1;
       }
       sort(a + 1, a + 1 + cnt, cmp);
       for (int i = 1; i <= cnt; i++)
       {
           if (a[i].t == 1)
               pos[++tot] = a[i].pos, num[tot] = a[i].num;
            if (a[i].t == -1)
            {
                int tmp = a[i].num;
                while (tmp)
                {
                    int num0;
                    int pos0 = pos[tot];
                    if (tmp >= num[tot])
                    {
                        num0 = num[tot];
                        tot--;
                        tmp -= num0;
                    }
                    else num0 = tmp, num[tot] -= tmp, tmp = 0;
                    long long k = a[i].pos - pos0, temp;
                    temp = ((long long)n * 2 - k + 1) / 2 * k % P;
                    temp = temp *(long long)num0 % P;
                    ans2 += temp;
                    ans2 = ans2 % P;
                }
            }
       }
       long long ans = (ans1 - ans2) % P + P;
       ans %= P;
       printf("Case #%d: %I64d\n", ++ca, ans);
    }
    return 0;

}
