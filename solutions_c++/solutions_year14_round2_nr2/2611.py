#include<cstdio>
int main()
{
    int t,i;
    long int a,b,k,res,l,m,x;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%ld%ld%ld",&a,&b,&k);
        res=0;
        for(l=0;l<a;l++)
        {
            for(m=0;m<b;m++)
            {
                x=l&m;
                if(x<k)
                {
                    res++;
                }
            }
        }
        printf("Case #%d: %ld\n",i,res);
    }
    return 0;
}
