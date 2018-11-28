#include<stdio.h>
#include<string.h>
#include<math.h>
int num[1002];
int square[1002];
void inital()
{
    memset(num,0,sizeof(num));
    memset(square,0,sizeof(square));
    int i,a,b;
    for(i=1;i<10;i++)
    {
        num[i] = 1;
        square[i*i] = 1;
    }
    for(i=10;i<100;i++)
    {   a = i/10; b = i%10;
        if(a==b)num[i] = 1;
        if(i*i<1000)
        {
            square[i*i] = 1;
        }
    }
    for(i=100;i<1000;i++)
    {
        a = i/100; b = i%10;
        if(a==b)num[i] = 1;
        if(i*i<1000)
        {
            square[i*i] = 1;
        }
    }
}
int main()
{
    int t,i,j,begin,end,x,n,sum;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("Fair_and_Square.txt", "w", stdout);
    inital();
    scanf("%d",&t);n=t;
    while(t--)
    {
        scanf("%d %d",&begin,&end);
        for(i=begin,sum = 0;i<=end;i++)
        {
            if(num[i]==1&&square[i]==1)
            {
                x =sqrt(i);
                if(num[x]==1)sum++;
            }
        }
        printf("Case #%d: %d\n",n-t,sum);
    }
    return 0;
}
