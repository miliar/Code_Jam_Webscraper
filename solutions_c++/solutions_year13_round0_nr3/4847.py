#include<stdio.h>
#include<math.h>

bool palincheck(long long int num)
{
    int ar[20],i=0,j=0,k=0;
    bool palin=true;
    while(num>0)
    {
        ar[i++]=num%10;
        num=num/10;
    }
    for(j=0,k=i-1;j<=k;j++,k--)
        if(ar[j]!=ar[k])
        palin=false;
    return palin;
}

int main()
{
    int t=0,tc=0;
    scanf("%d",&tc);

    for(t=1;t<=tc;t++)
    {
     long long int a=0,b=0,sqrta=0,sqrtb=0,i=0,counter=0,sqr=0;
     scanf("%lld%lld",&a,&b);
     sqrta=sqrt(a);
     sqrtb=sqrt(b);
     for(i=sqrta;i<=sqrtb;i++)
     {
         bool sqrtpalin=false,sqrpalin=false;
         sqrtpalin=palincheck(i);

         if(sqrtpalin)
            { sqr=i*i;
         if(sqr>=a&&sqr<=b)
            //printf("%lld\n",sqr);
            sqrpalin=palincheck(sqr);
               // printf("%d\n",sqrpalin);
            }
         if(sqrtpalin&&sqrpalin)
            counter++;
     }
       printf("Case #%d: %lld\n",t,counter);
    }


    return 0;
}

