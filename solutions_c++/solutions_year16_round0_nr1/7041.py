#include <iostream>
using namespace std;

int main() {
    long T,temp,cpy;
    int arr[10],a;
    cin>>T;
for(int i=1;i<=T;i++)
{  
    for(int k=0;k<10;k++)
    {
        arr[k]=0;
    }
    
    int num,j=1,count=0;
    cin>>num;
    while(1)
    {
     if(num==0)
     {
      cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
         break;   
     }
     temp=num*j;
     cpy=temp;
        while(temp!=0)
        {
            a=temp%10;
            arr[a]=1;
            temp=temp/10;
        }
     for(int z=0;z<10;z++)
     {
         if(arr[z])
         count++;
     }
     if(count==10)
     {
         cout<<"Case #"<<i<<": "<<cpy<<endl;
         break;
     }
     count=0;
     j++;
        
    }
    
    
    
    
    
}
	return 0;
}
