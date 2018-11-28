#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;


int n,t;
double v,x;
double r[101],c[101];
double eps=1e-12;


int main()
{
    int i,j,k,times;
    double v1,v2;
    
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    cin>>t;
    
    
    
    
    for(times=1;times<=t;times++)
    {
        cin>>n>>v>>x;
        
        for(i=1;i<=n;i++)
        {
            cin>>r[i]>>c[i];
        }
        
        
        cout<<"Case #"<<times<<": ";
        cout.precision(10);
        cout.setf(ios::fixed);
        if(n==1)
        {
            if(fabs(c[1]-x)<eps)
            {
                cout<<v/r[1]<<endl;
            }
            else
            {
                cout<<"IMPOSSIBLE"<<endl;
            }
        }
        else
        {
            if(c[1]>c[2])
            {
                swap(c[1],c[2]);
                swap(r[1],r[2]);
            }
            
            
            if(fabs(c[1]-x)<eps && fabs(c[2]-x)<eps)
            {
                cout<<v/(r[1]+r[2])<<endl;
            }
            else if(fabs(c[1]-x)<eps)
            {
                cout<<v/r[1]<<endl;
            }
            else if(fabs(c[2]-x)<eps)
            {
                cout<<v/r[2]<<endl;
            }
            else if(c[1]+eps<x && x+eps<c[2])
            {
                v1=((x-c[2])*v)/(c[1]-c[2]);
                v2=((x-c[1])*v)/(c[2]-c[1]);
                //cout<<v1<<' '<<v2<<"   vvv"<<endl;
                cout<<max(v1/r[1],v2/r[2])<<endl;
            }
            else
            {
                cout<<"IMPOSSIBLE"<<endl;
            }
            
        }
        
        
        
        
    }
    
    
    
    
    
    return 0;
}
