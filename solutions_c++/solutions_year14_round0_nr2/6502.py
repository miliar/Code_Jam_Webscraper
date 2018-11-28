#include <stdio.h>

int main()
{
    double c,f,x;
    int cases;
    double result;
    double temp;
    double time;
    bool cek=true;
    double rate;
    scanf("%d",&cases);
    int counter=1;
    while(cases-->0)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        rate=2.0;
        result=999999999;
        temp=0.0;
        time=0.0;
        while(time<result)
        {
            temp=(x/rate)+time;
            time+=c/rate;
            if(result>temp)
            {
                result=temp;    
            }
            rate+=f;
        }
        printf("Case #%d: %lf\n",counter,result);
        counter++;
    }
        
}
