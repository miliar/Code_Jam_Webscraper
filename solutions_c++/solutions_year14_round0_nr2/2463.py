#include<bits/stdtr1c++.h>
#include<stdio.h>
using namespace std;

#define eps 1e-9


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
        freopen("3.txt","w",stdout);
        
    #endif // ONLINE_JUDGE
    
   
    int t;
    cin>>t;
    int ic=1;
    while(t--)
    {
        double c,f,x;
        cin>>c>>f>>x;
        
        double ret=0;
        double r=2.0;
        while(1)
        {
            double d1=x/r;
            
            double d2=c/r + (x/(r+f));
            
            if(d1+eps < d2  || fabs(d1-d2)<eps)
            {
                ret+=d1;
                break;
            }
            else
            {
                ret+=c/r;
                r+=f;
            }
        
        }
        
        printf("Case #%d: %0.8lf\n",ic++,ret);
        
    }
    return 0;
    
}
