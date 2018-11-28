#include<stdio.h>
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long int tt;
    scanf("%lld", &tt);
    for (long long int qq=1;qq<=tt;qq++)
    {
        printf("Case #%lld: ", qq);
	   long long int a,i=0,b,z,c[10],count1=0;
        for(int k=0;k<10;k++)
            c[k]=0 ;
	    scanf("%lld",&a);
	    z=a;
        if(z!=0)
        {
	    while(count1!=10)
        {
            i++;
            a=z*i;
            while(a>0)
            {
                b=a%10;
                a=a/10;
                if(c[b]!=1)
                {
                    c[b]=1;
                    count1++;
                }
            }
        }
        printf("%lld\n",z*i);
        }
        else
            printf("INSOMNIA\n");

	}
	return 0;
}
