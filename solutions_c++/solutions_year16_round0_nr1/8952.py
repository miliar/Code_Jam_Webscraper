#include<stdio.h>
#include<iostream>
using namespace std;
 
long n,num;
int d,a[10],i,m=1,k=0,um,o=1;
void check();
void incre();
 
int main()
{
 scanf("%d",&um);
 while(o<=um)
       {
        m=1,k=0,um;
    scanf("%ld",&num);
    if(num==0)
    printf("\nCase #%d: INSOMNIA\n",o);
 
    else
    {
 for(i=0;i<10;i++)
 {
  if(i==0)
  a[i]=1;
  else
  a[i]=0;
 }
 incre();
 printf("Case #%d: %ld\n",o,n);
 }
       o++;
     }
 return 0;
}
 
void incre()
{
  m=1;
  k=0;
       do
       {
  n=m*num;
 
  check();
  m++;
 

       }while(k!=10);
 
}
 
void check()
{
 int temp;
 temp=n;
 while(temp>0)
 {
      d=temp%10;
      if(d!=0)
      {
      if(a[d]!=d)
      {
      a[d]=d;
      k++;
 
       }
  }
       if(d==0)
       {
       if(a[d]==1)
       {a[d]=0;
        k++;
 
       }
  }
     temp=temp/10;
 }
 }