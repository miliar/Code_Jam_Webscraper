#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <list>
#include <vector>
using namespace std;


int a[50];
bool pal(unsigned long long int t)
{
    int i=0;
    bool flag =true;
    while(t!=0)
    {
        a[i]=t%10;
        t/=10;
        i++;
        
        }
        i--;
    for(int j=0;j<=i/2;j++)
       if(a[j]!=a[i-j])
      { flag=false;
         //cout<<a[j]<<" "<<a[i-j]<<endl;
       break;
      }
      return flag; 
    
    
    }

int main()
{

    int test,total;
    cin>>total;
    test=1;
  
    while(test<=total)
     {
          unsigned long long int a,b,i,ans=0;
        long  double n,m;
       cin>>n>>m;
      
       
       a=(unsigned long long int)(sqrt(n));

      for( i=a*a; i<=m;)
         {
             
            
           // cout<<i<<a<<endl;
             if(i>=n)
             {
             if(pal(i)&&pal(a))
             ans++;
             }
             a++;
             i=a*a;
             
             }


cout<<"Case #"<<test<<": "<<ans<<"\n";
test++;

         }



    }

