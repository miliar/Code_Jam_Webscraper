#include <stdio.h>
#include <iostream>
#include <vector>
#define size 100
using namespace std;


int pal(int n)
{
    int temp=n,sum=0,r;
    while(temp>0)
    {
        r=temp%10;
        temp=temp/10;
        sum=sum*10+r;
    }
    if(sum==n)
    return 1;
    else return 0;
}        
    
    
    
int main()
{
    int t;
    cin>>t;
    vector<int> v;
        int i,n=0;
    for(i=1;i<=35;i++)
    {
        if(pal(i)&&(pal(i*i)))
        v.push_back(i*i);
    }    
    while(t--)
    { n++;
        int a,b,c=0;
        cin>>a>>b;
        
        for(i=0;v[i]<=b;i++)
        { 
            if(v[i]>=a)
        {
            //cout<<v[i]<<endl;
            c++;
         }    
        }    
     cout<<"Case #"<<n<<": "<<c<<endl;
  }
  return 0;
  
}      
