#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int t;
    scanf("%i",&t);
    int sum=0,cases=1,out=0;
        while(t--)
        {
            int smax;
            scanf("%i",&smax);
            char str[smax];
            scanf("%s",str);
            for(int i=1;i<=smax;i++)
            {  
             sum=sum+str[i-1]-48;
            
               if(sum<i)
               { if((i-sum)>out)
                    out=i-sum; 
               
                
                }
            }
           cout<<"Case #"<<cases<<": "<<out<<endl;
           cases++; 
           sum=0; 
           out=0; 
         }
}            
