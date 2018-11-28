#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define max 500


    
int main(){
    long long int T,m,num;
    cin>>T;
   for(int i=1;i<=T;i++)
   {
      cin>>m;
      if(m==0){
        num=0;
    }
    
    else
    {
        long long int s[10];
        for(int r=0;r<10;r++)
        {
           s[r]=-1;
        }
        for(int i=1;i<max;i++)
        {
           long long int temp=i*m;
            long long int S=temp;
        
            while(S!=0)
            {
                int res=S%10;
                s[res]=res;
                   
                S=S/10;
            }
          int flag=0;
        for(int k=0;k<10;k++)
        {
            if(s[k]!=-1)
            {
                flag=1;
            }
            else
            {    
                flag=0;
                break;
            }
                
       }
       if(flag==1)
       {
        
                num=temp;
                break;
        }
      }  
   }
    
       if(num!=0)
      cout<<"case #"<<i<<":"<<" "<<num<<endl;
      else
      cout<<"case #"<<i<<":"<<" "<<"INSOMNIA \n";   
   }
    return 0;
}