#include<stdio.h>
#include<string.h>
#include<math.h>

int main()
{
    double C,F,X,F1,total1,total,ans;
    long t,cas=1; 

    freopen("E:\\Codejam\\B.in","r",stdin);
    freopen("E:\\Codejam\\B.out","w",stdout);
    
    scanf("%ld",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        
        total=0;
        ans=0;
        F1=2;

        while(1)
        {

            total=X/F1;
            
            total1=C/F1;
            F1+=F;
            

            if(total<=total1+ X/F1)
                break;
  

            ans+=total1;
        }
        ans+=total;
    
    
        printf("Case #%ld: %.7lf\n",cas++,ans);        
    }


    return 0;    
}
