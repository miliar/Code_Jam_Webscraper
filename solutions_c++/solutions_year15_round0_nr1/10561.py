#include<iostream>
#include<stdio.h>
//#include<conio.h>
using namespace std;
int main()
 {
  freopen("abc.txt","r",stdin);
  freopen("xyz.txt","w",stdout);
  //clrscr();
  int T,j;
  cin>>T;
  for(j=1;j<=T;j++)
   {
  long long int n,a,s=0,p=0,i,b[8];
  cin>>n;
  cin>>a;
  for(i=n;i>=0;i--)
   {
    b[i]=a%10;
    a=a/10;
   }
  for(i=0;i<=n;i++)
   {
    if((i-p)>0&&b[i]>0)
     {
      s=s+(i-p);
      p=p+s;
     }
    p=p+b[i];
   }
  cout<<"Case #"<<j<<":"<<" "<<s<<"\n";
  }
  //getch();
  return 0;
 }