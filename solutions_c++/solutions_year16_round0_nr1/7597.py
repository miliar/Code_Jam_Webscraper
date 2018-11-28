#include<stdio.h>
int a[10];
bool check()
{
    int i,t=0;
    for(i=0;i<10;i++)
        if(a[i]==1)
        t++;
    if(t==10)
        return true;
    else
        return false;
}
int main()
{
    int T,u=1;
    scanf("%d",&T);
    while(T--)
    {
        int N,i,D,ans,c;
        scanf("%d",&N);
        D=N;
        for(i=0;i<10;i++)
            a[i]=0;
        c=0;
        i=1;
        while(i<=1000)
        {
            D=N*i;
            ans=D;
            while(D!=0)
            {
                a[D%10]=1;
                D=D/10;
            }
            if(check()==true)
                    {
                        c=1;
                        printf("Case #%d: %d\n",u,ans);
                        break;
                    }
            i++;
        }
        if(c==0)
            printf("Case #%d: INSOMNIA\n",u);
        u++;
    }
}
