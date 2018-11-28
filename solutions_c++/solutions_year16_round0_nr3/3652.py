#include<cstdio>
#include<cmath>
int num[33];
long long ans[11];
long long base(int b,int n)
{
    long long p=0,k;

    for(int i=0;i<n;i++)
    {
        p*=b;
        p+=(num[i]);
    }
  
   if(p%2==0) {
        ans[b]=2;
        return 2;
    }
    for(long long i=3;i<=(long long)sqrt(p);i+=2)
    {
        if(p%i==0)
        {
            ans[b]=i;
            return i;
        }
    }
    return 0;
}
int gen(long long now,int n)
{
    for(int i=n;i>=1;i--)
    {
        num[i]=now%2;
        now/=2;
    }
}
int main()
{
    int t;
    scanf("%d",&t);
    int N,J;
    scanf("%d%d",&N,&J);
    long long int sq;
    long long m=(long long)pow((double)2,(double)(N-2));
    int chk=0;
    num[0]=1; num[N-1]=1;
    printf("Case #1:\n");
    for(long long i=0;i<m;i++)
    {
        chk=0;
        gen(i,N-2);

        for(int j=2;j<=10;j++)
        {
            if(base(j,N)==0)
            {
                 chk=1;
                 break;
            }
        }
        if(chk==0)
        {

          
            for(int j=0;j<N;j++) printf("%d",num[j]); printf(" ");
            for(int j=2;j<=10;j++)
                printf("%lld ",ans[j]);
            printf("\n");
            J--;
            if(J<=0) return 0;
        }
    }
    return 0;
}
