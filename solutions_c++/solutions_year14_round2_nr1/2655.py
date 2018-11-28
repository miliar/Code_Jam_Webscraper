#include<iostream>
using namespace std;
int main()
{
 char s1[102],s2[102],t1[102],t2[102];
 
 int t,n;
 int x=1;
 cin>>t;
 while(t--)
 {
  cin>>n;
  cin>>s1>>s2;
  int i=0,j=0;
  for(i=0,j=0;i<strlen(s1);j++)
  {
   t1[j]=s1[i];
   i++;
   while(s1[i]==t1[j])
   i++;   
  }
  t1[j]='\0';
  
  i=0,j=0;
  for(i=0,j=0;i<strlen(s2);j++)
  {
   t2[j]=s2[i];
   i++;
   while(s2[i]==t2[j])
   i++;   
  }
  t2[j]='\0';
    
  
  
  if(strcmp(t1,t2)!=0)
  cout<<"Case #"<<x<<": "<<"Fegla Won\n";
  
  else
  {
      int count=0;
       for(int i=0,j=0;i<strlen(s1);)
       {
        int count1=0,count2=0;
        
        
        char cs1=s1[i],cs2=s2[j];
        
        while(s1[i]==cs1)
        {
         count1++;
         i++;
        }
        
        while(s2[j]==cs2)
        {
         count2++;
         j++;
        }
        count+=abs(count1-count2);
       }
     cout<<"Case #"<<x<<": "<<count<<"\n";  
  }
  x++;
 }
 
}
