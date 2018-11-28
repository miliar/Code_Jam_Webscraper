#include <iostream>

using namespace std;

#define max 2147483647


int main()
{
    int t, i;
    double c, f, x ;
    double temp, res, pre;
    double rate = 2;
    
    scanf("%d",&t);
    for(i=1; i<= t ;i++)
    {
        rate  = 2;
        scanf("%lf%lf%lf",&c,&f,&x);
        
        temp =  x / rate;
        res = max;
        pre = 0;
        while(res > temp)
        {
            res = temp;
            pre +=  c / rate;
            rate += f;
            temp = pre + x/rate;                
        }
        
        printf("Case #%d: %0.7lf",i,res);
        if(i!=t) printf("\n");
        
    }
   
   return 0;
}
