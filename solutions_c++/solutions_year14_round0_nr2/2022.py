#include<iostream>
using namespace std;
int main()
{
    

    freopen("B-large.in","r",stdin);
    freopen("outer3.txt","w",stdout);
     int cases;
    
    scanf("%d",&cases);
    for(int c =1;c<=cases;c++)
    {
            
            double C, F , X;
           // cin>>C;
            //cin>>F;
            //cin>>X;
            scanf("%lf",&C);
            scanf("%lf",&F);
            scanf("%lf",&X);
            double ans = 0;
            double present = 2;
            double next = 0;
            double cost1 ;
                    
                    double pct ;
                    double npresent ;
                    double nct  ;
                    double cost2 ; 
            if(X<=C)
            {
                    ans  =  X/2;
                    
            }
            else
            {
            while(1)
            {
                     cost1 =  X/present;
                     pct = C/present;
                     npresent = (present + F);
                     nct  =  X/npresent ;
                     cost2  =  pct +  nct;
                    if(cost1<=cost2)
                     {ans = ans  +  cost1;
                     break;}
                    else if(cost1>cost2)
                     {ans = ans + pct;
                       present = npresent;
                     }
                     //<<endl;
            }
            
            }
            //cout<<ans<<endl;
            printf("Case #%d: %0.7lf\n",c,ans); 
    }
    return 0;
}
