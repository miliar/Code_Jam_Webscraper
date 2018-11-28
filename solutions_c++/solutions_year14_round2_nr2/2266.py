#include<stdio.h>
int A,B,K;
int getans()
{
    int t=0;//printf("a=%d,b=%d,k=%d\n",A,B,K);
    for(int i=0;i<A;i++)
        for(int j=0;j<B;j++)
        if((i&j)<K)
    {
       // printf("i=%d,j=%d,i&j=%d\n",i,j,i&j);
        t++;
    }
    return t;
}
int main()
{
   // freopen("2.in","r",stdin);
   //freopen("2.txt","w",stdout);
    int T,t=1,ans;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&A,&B,&K);
        ans=getans();//return 0 ;
        printf("Case #%d: %d\n",t++,ans);
    }
    return 0;
}
