#include<iostream>

using namespace std;

int main()
 {
  int r=0,total=0,i=0,j,n,test,m;
  char s[6];
  cin>>test;
  for(j=0;j<test;j++)
   {   
    r=total=0;
    cin>>m;  
    cin>>s;
  for(i=0;i<=m;i++)
   {
    if(total<i&&s[i]!='0') 
     {
      r+=i-total;
      total+=r;    
     }  
    total+=s[i]-48; 
   }
     cout<<"case #"<<j+1<<": "<<r<<endl;
   } 
 
   return 0; 
   
 }