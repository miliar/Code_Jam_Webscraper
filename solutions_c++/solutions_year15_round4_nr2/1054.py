#include <bits/stdc++.h>
using namespace std;

#define cin(n) scanf("%d",&n)
#define eps 1e-12
double a[9],b[9];

int main() 
{
    int t,m,n,i,j,k,l;
    
    cin(t);
    int ct=1;
    while(t--)
    {
        double v,x;
        cin>>n>>v>>x;
        
        
        cout<<"Case #"<<ct++<<": ";
        for(i=0;i<n;i++)
            cin>>a[i]>>b[i];
        
        if(b[0]==b[1])
        n=1;
        if(n==1)
        {
            double ans=v/a[0];
            if(b[0]==x)
                printf("%.6lf\n",ans);
            else
                printf("IMPOSSIBLE\n");
            continue;
        }    
        
        if(b[0]>b[1])
        {
            swap(a[0],a[1]);
            swap(b[0],b[1]);
        }    
        double low,high;
        
        
        
        double v1=x*v-v*b[1];
        double v2=b[0]-b[1];
        
        low=v1/v2;
        
        if(low<0.0)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }    
        
        double ans=max((low/a[0]),((v-low)/a[1]));
        printf("%.6lf\n",ans);
        
        
        
    }    
    return 0;
}
