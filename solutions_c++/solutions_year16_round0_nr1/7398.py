#include<cstdio>

int m;
int x;
int chk[15];

void tryCheck(int i)
{
    int y = i;
    while(y >= 10)
    {
        if(chk[y%10] == 0)
        {
            chk[y%10] = 1;
            m++;
            //printf("eiei %d\n",m);
        }
        y /= 10;
    }
    //printf("%d\n",chk[y%10]);
    if(chk[y%10] == 0)
    {
        chk[y%10] = 1;
        m++;
        //printf("eiei %d\n",m);
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("eq.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int round = 1;round<=n;round++)
    {
        m = 0;
        for(int i=0;i<=9;i++)
        {
            chk[i] = 0;
        }
        scanf("%d",&x);
        if(x == 0)
        {
            printf("Case #%d: INSOMNIA\n",round);
            continue;
        }
        int temp = x;
        while(m < 10)
        {
            tryCheck(x);
            if(m < 10)
                x += temp;
            //printf("%d %d %d\n",x,temp,m);
        }
        printf("Case #%d: %d\n",round,x);
    }
}
