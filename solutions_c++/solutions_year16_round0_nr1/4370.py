#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++)
    {
        int n;
        bool num[11];
        scanf("%d",&n);
        printf("Case #%d: ",cas);
        if(n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        memset(num,false,sizeof(num));
        for(int i = 1;;i++)
        {
            int x = n * i;
            while(x)
            {
                num[x%10] = true;
                x /= 10;
            }
            bool flag = true;
            for(int j = 0; j <= 9; j++)
                if(!num[j]) flag = false;
            if(flag)
            {
                printf("%d\n",n * i);
                break;
            }
        }
    }
    return 0;
}
