#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

long long p[110] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
int cntp;

/*bool isPalin(long long num)
{
    char a[20];
    long long tmp = num;
    int cnt = 0;
    while(tmp)
    {
        a[cnt ++] = tmp % 10 + '0';
        tmp /= 10;
    }
    for(int i = 0; i < cnt; i ++)
        if(a[i] != a[cnt - 1 - i])
            return false;
    return true;
}

void pre(long long ed)
{
    for(long long i = 1; i <= ed; i ++)
    {
        long long tmp = i * i;
        if(isPalin(tmp) && isPalin(i))
            p[cntp ++] = tmp;
    }
}*/

int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
   // memset(p, 0, sizeof(p));
    cntp = 39;
   // pre(end);
    int t = 1, cse;
    scanf("%d", &cse);
    while(cse --)
    {
        long long st, ed;
        scanf("%lld%lld", &st, &ed);
        int ans = 0;
        for(int i = 0; i < cntp; i ++)
        {
            if(st <= p[i] && ed >= p[i])
                ans ++;
        }
        printf("Case #%d: %d\n", t ++, ans);
    }
}
