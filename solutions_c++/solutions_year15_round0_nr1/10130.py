#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int t,i,inx,flag=0,j,shy_max,sum,people;

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
   cin>>t;
  // int shy[1000];
j=0;
   
    while(j++<t)
    { sum=0;

        people=0;
       //cout<<"the value of t"<<t;    
        cin>>shy_max;
    
        string shy;
        cin>>shy;
        //cout<<shy;

        // for(i=0;i<=shy_max;i++)
        // {

        // cin>>shy[i];
        // }

        // for(i=0;i<=shy_max;i++)
        // {
        // cout<<shy[i];
        // }
       // cout<<"\n";
         for(i=0;i<=shy_max ;i++)
        
         {

        if(shy[i]-48==0)
        continue;

        else if(i>sum)
            {
            people=people+(i-sum);
            //cout<<"needed more is "<<(i-sum)<<"\n";
            sum=sum+(people);
            //cout<<"sum inside condition is "<<sum<<"\n";
            }


        sum=sum+shy[i]-48;
        //cout<<"sum outside condition is "<<sum<<"\n";
      
        }
        
    cout<<"case #"<<j<<":"<<" "<<people<<"\n";
   
        //cout<<"\n";

            
      
    }
   return 0; 
}
    
