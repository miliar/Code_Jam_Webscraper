#include<stdio.h>
//#include<conio.h>

int main()
{
    int t,k;
    double c,f,x,i;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
                     double sum =0,a=0,b=0,q=0,d=0;
                     
                     scanf("%lf %lf %lf",&c,&f,&x);
                     if(c>x)
                     {
                            sum = sum + x/2;
                            printf("Case #%d: %.7lf\n",k,sum);
                     }
                     else
                     {
                     d = x-c;
                     for(i=2;;i=i+f)
                     {
                                    a = d/i;
                                    //printf("%f\n",a);
                                    b = x/(i+f);
                                    //printf("%f\n",b);
                                    //getch();
                                    if(b<a)
                                    {
                                           q = c/i;
                                           sum = sum + q;
                                           //printf("%f\n",sum);
                                           //getch();
                                    }
                                    
                                    else
                                    {
                                        sum = sum + (x/i);
                                        //printf("%f\n",sum);
                                        break;
                                    }
                     }
                     printf("Case #%d: %.7lf\n",k,sum);
                     }
                     
                     
    }
    //getch();
    return 0;
}             
    
