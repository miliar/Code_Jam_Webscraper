#include<bits/stdc++.h>
using namespace std;
int main()
{
 int t,k=0;
 cin>>t;
 k=1;
 while(t--)
     {
       long num,value=1;
       set<int>s;
       cin>>num;
       long temp;
       bool flag=false;
       for(int i=1;i<100;i++)
       {
         if(s.size()==10)
         {
             flag=true;
             break;
             value=i-1;
         }
         temp=i*num;
         while(temp)
         {
           int d=temp%10;
           s.insert(d);
           temp=temp/10;
         }
       }
       if(flag)
       cout<<"Case #"<<k<<": "<<value*num<<endl;
       else
       cout<<"Case #"<<k<<": "<<"INSOMANIA\n";
    k++;
     }
}
