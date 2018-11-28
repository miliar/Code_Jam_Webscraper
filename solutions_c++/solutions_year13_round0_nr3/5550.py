#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
int palind(double n)
{
 long i,k,j=0;
 i=n;

 if(i==n)
 {
 while(i>0)
 {
  k=i%10;
  j=j*10+k;
  i=i/10;
 }
 if(n==j)
  return 1;
 else
  return 0;
 }
 else
  return 0;
 }
 void main()
 {
 clrscr();
  freopen("c.in","r",stdin);
  freopen("c2.out","w",stdout);
  double n,a,b,i,j,l,o[1000],m=0;
  cin>>n;
  while(n>0)
  {
   int status=0;
   l=0;
   cin>>a;
   cin>>b;
    for(i=a;i<=b;i++)
   {
    if(palind(i))
    {
     if(palind((sqrt(i))))
      status=1;
     else
      status=0;
    }
    else
      status=0;
       if(status==1)
	l++;
   }
   o[m]=l;
   m++;
   n--;
  }
  clrscr();
  for(j=0;j<m;j++)
   cout<<"Case #"<<j+1<<": "<<o[j]<<endl;

  getch();

 }



