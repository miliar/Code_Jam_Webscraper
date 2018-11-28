#include <cstdio>
#include <cstdlib>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output22.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    
    for(int c = 1; c <= cases ; c++)
    {
        double C, F, X, xtime= 0,ctime=0,time1,time2,time_prev=0,ans;
        double v = 2;
        
        scanf("%lf%lf%lf",&C,&F,&X);
        
        while(1)
        {
            time1 = time_prev + X/v;
            
            time2 = time_prev + C/v;
            v = v + F;
            time2 = time2 + X/v;
            
            if(time1<=time2)
            {
                ans = time1;
                break;
            }
            else
            {
                time_prev = time2-X/v;
                continue;
            }
        }
        
        printf("Case #%d: %.7lf\n",c,ans);
        
    }
    return 0;
}