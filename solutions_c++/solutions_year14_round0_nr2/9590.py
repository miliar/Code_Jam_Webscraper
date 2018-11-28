//bansal0301
#include<stdio.h>
#include<algorithm>
int main()
{
    int t,n,i,j,k;
    double temp1,temp2 ,ans,c,f,x;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        temp2=x/2.0;
        i=0;
        do
        {
            temp1=temp2;
            //printf("%lf temp1 \n",temp1);
            temp2=0;
            i++;
            for(j=0;j<i;j++)
            {
                temp2=temp2+((c)/(2.0+j*f));

            }
            //printf("%lf temp2",temp2);
            temp2=temp2+((x)/(2.0+(i*f)));
            //printf("%lf temp2 \n",temp2);
        }while(temp1>temp2);
        printf("Case #%d: %.7lf \n",k,temp1);

    }
return 0;
}
