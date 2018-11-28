 //FUCK

#include<stdio.h>

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

    int t,n;
    long long p;
    scanf("%d",&t);

    for(int tt=0;tt<t;tt++)
    {
        scanf("%d %lld",&n,&p);
        
        long long reta=0;
        int flag=0;
        for(int i=n-1;i>=0;i--)
        {
            long long pp=p-1;
            long long test=pp&(((long long)1)<<i);
            if(test==0)
            {
                int mm=n-i;
                reta=(((long long)1)<<(mm))-2;
                flag=1;
                break;
            }
        }
        if(!flag)
        {
            reta=p-1;
        }


        long long retb=0;
        flag=0;
        for(int i=n-1;i>=0;i--)
        {
            long long test=p&(((long long)1)<<i);
            if(test)
            {
                int mm=n-i;
                retb=(((long long)1)<<n)-(((long long)1)<<(mm));
                flag=1;
                break;
            }
        }
        if(!flag)
        {
            retb=p-1;
        }


        printf("Case #%d: %lld %lld\n",tt+1,reta,retb);
    }
}
