

#include <iostream>
#include<string>
#include<cmath>
using namespace std ;


int main ()
{
    int T;cin>>T;
    int b[T];
    for(int t=0;t<T;t++)
    {
        string N;
        cin>>N;
        int a[N.size()],x=0,cnt=0;
        for(int i=0;i<N.size();i++)
        {
            a[i]=N[i];
            
        }
        for(int j=1;j<N.size();j++)
        {
            if(a[0] == a[j])
            {x++;}
            else
            { for(int k=0;k<=x;k++)
            { a[k]=a[j];}cnt++;
                
            }
        }
        if(a[0]==45)
        {b[t]=cnt+1;}
        else
        {b[t]=cnt;}
    }
    
    for(int t=0;t<T;t++)
        cout<<"Case #"<<t+1<<":"<<" "<<b[t]<<endl;
    
    
}




