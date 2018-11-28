#include<bits/stdc++.h>
using namespace std;

int main() {
  long long int t,i,n,j,f,r,q,k,x,u,z=0,a[100000],b[100000];
    cin>>t;
    for(i=0;i<t;i++)
        {
        cin>>n;f=1;z=0;
        for(j=0;j<n;j++)
          cin>>a[j];        
        while(f!=0)
            { 
          r=*max_element(a,a+n);  
            if(r==0)
            {f=0;break;}
        k=distance(a,max_element(a,a+n));
        b[z]=k;z++;
        a[k]=a[k]-1;
           }
        cout<<"Case #"<<i+1<<": ";
        if(z%2==0)
            {
        for(j=0;j<z;j++)
            {
              if(j%2==0)                              
             cout<<char(b[j]+65);                 
             else                                              
             cout<<char(b[j]+65)<<" ";                          
           } 
          }
        else
            {
              u=z-3;
            for(j=0;j<u;j++)
              {
              if(j%2==0)                              
             cout<<char(b[j]+65);                 
             else                                              
             cout<<char(b[j]+65)<<" ";                          
              }
             for(;j<z;j++)
                 {
                   if(j%2!=0)                              
             cout<<char(b[j]+65);                 
             else                                              
             cout<<char(b[j]+65)<<" ";  
                }
           }
        cout<<endl;        
    }   
    return 0;
}