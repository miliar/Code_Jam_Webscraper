#include<stdio.h>
#include<iostream>
#include<string.h>
#include <math.h>
using namespace std;
int reverse(long num){
   long x,rev; 
   int dig;
   x = num;
   rev = 0;
   while (num > 0)
   {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
  }
  if(x==rev) 
    return 1;
  else
    return 0;
}
int main(void)
{
    int round,count;
    long a,b;
    double c;
    cin>>round;
    for(int i=1;i<=round;i++){
        count=0;    
        cin>>a;
        cin>>b;    
        for(int j=a;j<=b;j++){
            if(reverse(j)){
              c = sqrt(j);             
              if((int(c) == c)&& reverse(c)){
                count++;                
                }
            }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
