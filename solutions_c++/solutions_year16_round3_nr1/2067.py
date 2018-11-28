#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++)
    {
        int n;
        int num[30];
        scanf("%d",&n);
        int total = 0;
        for(int i = 0; i < n; i++)
        {
            scanf("%d",&num[i]);
            total += num[i];
        }
        printf("Case #%d:",cas);
        while(total)
        {
            int x = -1,y = -1;
            int maxx = 0;
            for(int i = 0; i < n; i++)
            {
                if(num[i] && maxx < num[i])
                {
                    maxx = num[i];
                    x = i;
                    y = -1;
                }
                else if(num[i] && maxx == num[i])
                {
                    y = i;
                }
            }
            num[x]--;
            total--;
            printf(" %c",x + 'A');
            if(y != -1 && maxx * 2 > total)
            {
                num[y]--;
                total--;
                printf("%c",y + 'A');
            }
        }
        printf("\n");
    }
    return 0;
}
