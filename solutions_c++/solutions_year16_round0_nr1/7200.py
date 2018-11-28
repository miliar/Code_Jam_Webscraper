#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int t;
    cin>>t;
    for(int p=0;p<t;p++)
        {
    int n;
    cin>>n;
    int count[10];
    int flag=0;
    int k=1;
 
        for(int l=0;l<10;l++)
            count[l]=0;
    while(1)
    {
      
        flag=0;
     
       
        int temp=k*n;
        int temp2=temp;
        while(temp>0)
        {
            int rem=temp%10;
                temp=temp/10;
                count[rem]=1;
        }
        
        for(int i=0;i<10;i++)
            flag=flag+count[i];
        
        k++;
        
        if(flag==10)
        {  cout<<"Case#"<<p+1<<":"<<" "<<temp2<<endl;
           break;
        }
        if(n==0)
        {  cout<<"Case#"<<p+1<<":"<<" "<<"INSOMNIA"<<endl;
           break;
        }
    }
      
    }
    return 0;
}
