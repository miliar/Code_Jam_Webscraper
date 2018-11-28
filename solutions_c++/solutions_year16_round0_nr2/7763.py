#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
  int t,i;
   /*freopen("B-large.in","rt",stdin);
  freopen("sushilOutput.cpp","wt",stdout);*/
  cin>>t;
  for(i=1;i<=t;i++)
  {
    char s[101];
    cin>>s;
    int j,count=0;
    int lstmns=103;
     for(j=0;j<strlen(s);j++)
     {
       if(s[j]=='-')
       {
         if(j!=lstmns+1)
         {
             count++;lstmns=j;
         }
         else
         {
             lstmns = j;
         }
       }
     }
     if(s[0]=='+')
     {
      cout<<"Case #"<<i<<": "<<2*count<<endl;
     }
     if(s[0]=='-')
     {cout<<"Case #"<<i<<": "<<2*count-1<<endl;}
  }
}
