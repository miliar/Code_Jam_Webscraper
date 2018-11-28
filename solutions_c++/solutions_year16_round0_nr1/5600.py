#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
    {
    long long int t,i,n,s,j,p,k,f=1,z,q=0,count[100000]={0};
    cin>>t;
    for(i=0;i<t;i++)
        {
          cin>>n;s=n;f=1;q=0;long long int count[100000]={0};
           for(j=1;q<1;j++)
               {
                 s=n*j;f=1;
                 if(s<10)
                     count[s]++;
                 else
                     {
                       p=s;
                       while(p>0)    
                       {
                           k=p%10;count[k]++;p=p/10;
                       }
                     }
                  for(z=0;z<=9;z++)
                      {
                     if(count[z]==0)
                         {
                          f=0;break; 
                        }
                     }
                 if(f==1)
                 {q=1;cout<<"Case #"<<i+1<<": "<<s<<endl;}
                 else if(s==0)
                     {q=1;cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";}
               }
        }    
    return 0;
}