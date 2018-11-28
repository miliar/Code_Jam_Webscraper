#include<stdio.h>
int T;
long long A,B,C;
long long a[111];
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dsmall.txt","w",stdout);
    int i,j,k;
    long long p,q,r;
    scanf("%d",&T);
for(int ii=0;ii<T;ii++)
{
    scanf("%I64d %I64d %I64d",&A,&B,&C);
    for(i=0;i<A;i++)a[i]=i+1;
    p=A;
    for(i=0;i<B-1;i++)
    {
        q=0;
        for(j=0;j<A;j++)
        {
            a[j]+=q;
            q+=p;
        }
        p+=A;
    }

    printf("Case #%d: ",ii+1);
    for(i=0;i<A;i++)printf("%I64d ",a[i]);printf("\n");
}


    return 0;
}
