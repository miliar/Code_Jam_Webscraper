#include<iostream>

using namespace std;

int main()
 {
  int r=0,tot=0,i=0,j,n,t,m;
  char str[6];
  cin>>t;
  for(j=0;j<t;j++)
   {   
    r=tot=0;
    cin>>m;  
    cin>>str;
  for(i=0;i<=m;i++)
   {
    if(tot<i&&str[i]!='0') 
     {
      r+=i-tot;
      tot+=r;    
     }  
    tot+=str[i]-48; 
   }
     cout<<"case #"<<j+1<<": "<<r<<endl;
   } 
 
   return 0; 
   
 }