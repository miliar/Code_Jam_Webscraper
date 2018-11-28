#include<cstdio>
#include<algorithm>
 
using namespace std;
int main()
{
        int i,t;
        double c,f,x;
        scanf("%d",&t);
        for(i=1;i<=t;i++)
        {       //double t=0,sum1=0,sum2=0,sum3=0,sum4=0,sum41=0,sum42=0;
                double rate,c,f,x,t=0;
				scanf("%lf%lf%lf",&c,&f,&x);
                rate=2;
                //t=0;
                double ckie=0;
                t=min(x/rate,c/rate);
                ckie=2*t;
                while(ckie<x)
                {
                	if((x-c)/rate*(rate+f)>x)
                	{
                		rate+=f;
                		t+=c/rate;
                		ckie=c;
                	}
                	else
                	{
                		t+=(x-ckie)/rate;
                		ckie=x;
                	}
        
                	
                
                }
                //t+=x/rate;
                /*if(x<=c)
                {
                        sum1=x/t;
                        printf("Case #%d: %.7lf\n",i,sum1);
                        continue;
                }
                int count=0;
                do
                {       if(count==0)
                        {
                        sum1+=c/(t+(count)*f);
                        sum2=x/(t+(count)*f);
                        sum3=c/(t+(count+1)*f);
                        sum4=x/(t+(count+1)*f);
                        sum41=sum1+sum3+sum4;
                        sum42=sum2;
                        sum1+=sum3;
                        }
                        else
                        {
                                //sum1+=c/(t+(count+1)*f);
                                sum2=x/(t+(count+1)*f);
                                sum42=sum41;
                                sum41=sum1+sum2;
                                sum1+=c/(t+(count+1)*f);
                               
                        }
                        count++;
                }while(sum41<sum42);*/
                  printf("Case #%d: %.7lf\n",i,t);    
             //   else if(count>1)
           //       printf("Case #%d: %.7lf\n",i,sum42);    }
        }
}
