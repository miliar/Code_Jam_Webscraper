#include <algorithm>
#include <iostream>
#include<cstdlib>
//#include<cstring>
//#include<string.h>
#include<cmath>
using namespace std;
int chkpalin(int n)
{   int rev=0,r=0,num;
    num=n;
    while(num!=0)
    {
        r=num%10;
        num=num/10;
        rev=rev*10+r;
        }
    if(rev==n)
    return 1;
    else 
    return 0;
    
    }
int main()
{
  
    //char buffer[3000];
    int l,h,i,test,cases,n,c,c2,count=0,s;
   
    cin>>cases;
    for(test=0; test<cases; test++)
    {
       count=0;
       c=0;c2=0;
        cin>>l>>h;
      
        if(l==(int)sqrt(l)*(int)sqrt(l))
        i=l;
        else
        i=((int)sqrt(l)+1)*((int)sqrt(l)+1);
        
        for(i;i<=h;(i=(i)+2*(int)sqrt(i)+1))
        {
            
             c=chkpalin(i);
             c2=chkpalin((int)sqrt(i));
           if(c==1 && c2==1)
           count++;
        }
        
        
       
        cout<<"Case #"<<test+1<<": "<<count<<endl;
    }
   // system("pause");
    return 0;
}
