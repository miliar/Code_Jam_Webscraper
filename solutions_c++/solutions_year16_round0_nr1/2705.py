#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdio>
#include<vector>
#include<map>

#define maxn 1000000
using namespace std;

int f[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w", stdout);
    int T;
    scanf("%d", &T);
    for (int kase=1;kase<=T;kase++)
    {
        int n;
        scanf("%d", &n);
        int flag = 0;
        int ans;
        memset(f, 0, sizeof(f));
        for (int i=1;i<=100;i++)
        {
            int tmp = n * i;
            ans = tmp;
            while (tmp > 0)
            {
                int x = tmp % 10;
                flag = flag + 1 - f[x];
                f[x] = 1;
                tmp = tmp / 10;
                if (flag == 10) break;
            }
            if (flag == 10) break;
        }
        printf("Case #%d: ",kase);
        if (flag == 10) printf("%d\n", ans);
        else printf("INSOMNIA\n");
    }
    return 0;
}
