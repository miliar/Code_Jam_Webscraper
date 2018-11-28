#include <bits/stdc++.h>
using namespace std;

#define cin(n) scanf("%d",&n)
#define eps 1e-12
double a[9],b[9];

int main() 
{
    int t,m,n,i,j,k,l;
    
    cin(t);
    
    while(t--)
    {
        double v,x;
        cin>>n>>v>>x;
        
        
        
        for(i=0;i<n;i++)
            cin>>a[i]>>b[i];
        
        if(b[0]>b[1])
        {
            swap(a[0],a[1]);
            swap(b[0],b[1]);
        }    
        double low,high;
        
        high=v;
        low=0.;
        
        double ans=0.0;
        while((high-low)>1e-6)
        {
            double mid=(low+high)/2.;
            
            double vl=mid*b[0]+(v-mid)*b[1];
            vl/=v;
            
            if(vl==x)
                break;
            if(vl+eps<=(x))
                high=mid;
            else
                low=mid;
        }
        
        low=(low+high)/2.0;
        //cout<<low<<"\n";
        ans=(low/a[0])+((v-low)/a[1]);
        printf("%.6lf\n",ans);
        
        high=v;
        low=0.;
        
        ans=0.0;
        while((high-low)>1e-6)
        {
            double mid=(low+high)/2.;
            
            double vl=mid*b[0]+(v-mid)*b[1];
            vl/=v;
            
            if(vl==x)
                break;
            if(vl+eps>=(x))
                high=mid;
            else
                low=mid;
        }
        
        low=(low+high)/2.0;
        //cout<<low<<"\n";
        ans=(low/a[0])+((v-low)/a[1]);
        printf("%.6lf\n",ans);
        
    }    
    return 0;
}
