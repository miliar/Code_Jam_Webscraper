#include<iostream>

using namespace std;

int main()
 {
  int req=0,total=0,i=0,j,num,t,max;
  char str[6];
  cin>>t;
  for(j=0;j<t;j++)
   {   
    req=total=0;
    cin>>max;  
    cin>>str;
  for(i=0;i<=max;i++)
   {
    if(total<i&&str[i]!='0') 
     {
      req+=i-total;
      total+=req;    
     }  
    total+=str[i]-48; 
   }
     cout<<"case #"<<j+1<<": "<<req<<endl;
   } 
 
   return 0; 
   
 }