#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main()
{
    int t,x,r,c,p=0;
    scanf("%d",&t);
    while(t--)
    {
     p++;
     scanf("%d%d%d",&x,&r,&c);
     if(x==1){cout<<"case #"<<p<<": "<<"GABRIEL"<<endl;continue;}
     if(x==4)
     {
      if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))       
     {cout<<"case #"<<p<<": "<<"GABRIEL"<<endl;continue;}
     else
      {cout<<"case #"<<p<<": "<<"RICHARD"<<endl;continue;}}
      if(x==3)
      {
     if((r==1 || c==1) || (c==2 && r==2) || (r==2 && c==4)||(r==4 && c==2) || (r==4 && c==4))   
     {cout<<"case #"<<p<<": "<<"RICHARD"<<endl;continue;}
     else 
     {cout<<"case #"<<p<<": "<<"GABRIEL"<<endl;continue;}}
     if(x==2)
     {
     if((r==1 && c==1) || (r==1 && c==3) || (r==3 && c==1)||( r==3 && c==3 )) 
      {cout<<"case #"<<p<<": "<<"RICHARD"<<endl;continue;}
      else
      {cout<<"case #"<<p<<": "<<"GABRIEL"<<endl;continue;}}
      }
  return 0;
}     
