#include<stdio.h>
#include<stdlib.h>
int main()
{
    double i,j,k,l,m,n,p,q,c,a,b,d,t,r,x,f,y,time;
    scanf("%lf",&t);
    for(p=0;p<t;p++)
    {
                    time=0;
                    scanf("%lf%lf%lf",&c,&f,&x);
                    k=2;
                    while(1)
                    {
                           l=x/k;
                           a=c/k;
                           b=k+f;
                           d=a+(x/b);
                          // printf("%lf %lf\n",l,d);
                           if(l>d)
                           {
                                  k=b;
                                  time+=a;
                           }
                           else
                           {
                                time+=l;
                                break;
                           }
                    }
                    printf("Case #%.0lf: %.7lf\n",p+1,time);
    }
    //system("pause");
    return(0);
}      
                             
