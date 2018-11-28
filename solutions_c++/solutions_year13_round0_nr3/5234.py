#include <stdio.h>
#include <math.h>
#include <string.h>
#define N 100000

int a[N];

int judge1(int n)
{
    int  sum = 0;
    while(n)
    {
        sum = sum*10 + n%10;
        n /= 10;
    }
    //printf("%d\n",sum);
    return sum;
}

void list1()
{
    memset(a,0,sizeof(a));
    int i = 0;
    a[0] = 0;
    for(i = 1; i < N; i++)
        if(i == judge1(i))
            {
                double x = sqrt(i);
                double y = x - (int)x;

                if(y < 0.0000001)
                    {
                        int z = (int)x;
                     if(z == judge1(z))
                        a[i] = a[i-1]+1;
                     else
                        a[i] = a[i-1];
                    }
                    else
                        a[i] = a[i-1];
            }
        else
            a[i] = a[i-1];

    /*for(i = 1; i< 100; i++)
        printf("%d  ",a[i]);
        printf("\n");*/
}
int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    list1();
    int t = 0;
    int w = 0;
    scanf("%d",&t);
    for(w = 1; w <= t; w++)
    {
        int x,y;

        scanf("%d%d",&x,&y);
        printf("Case #%d: ",w);
        printf("%d\n",a[y] - a[x-1]);

    }
    return 0;
}
