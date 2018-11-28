#include<stdio.h>
#include<string.h>
int map[10][10];
int a[20];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,m,x,d,Case = 1;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d",&m);
        memset(a,0,sizeof(a));
        for(int i = 1;i <=4;i++)
        {
            for(int j = 1;j <= 4;j++)
            {
                scanf("%d",&d);
                if(i==m)
                {
                    a[d] = 1;
                }
            }
        }
        scanf("%d",&x);
        int num = 0;
        int p = 0;
        for(int i = 1;i <=4;i++)
        {
            for(int j = 1;j <= 4;j++)
            {
                scanf("%d",&d);
                if(i==x)
                {
                    if(a[d])
                    {
                        num++;
                        p = d;
                    }
                }
            }
        }
        printf("Case #%d: ",Case++);
        if(num == 1)
        {
            printf("%d\n",p);
        }
        else if(num == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
}
