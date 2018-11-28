#include<stdio.h>
int main()
{
     freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,i,j,k;
    scanf("%d",&t);
    int a[10],s;

    for(i=0;i<t;i++)
    {

         for(j=0;j<10;j++)
            a[j]=j;
        int n,m;
        long long int p,q;
        s=55;
        scanf("%d",&n);

        if(n==0)
            printf("Case #%d: INSOMNIA\n",i+1);
        else
        {

     for(k=1;s!=110;k++)
     {
         p=k*n;
         q=k*n;
    for(j=0;p!=0;j++)
    {
        m=p%10;
        p=p/10;

        a[m]=11;
    }
    s=0;
    for(j=0;j<10;j++)
        s=s+a[j];

    }
           printf("Case #%d: %lld\n",i+1,q);
    }

    }
    return 0;
}

