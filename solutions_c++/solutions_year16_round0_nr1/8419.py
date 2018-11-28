#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

void main()
{
 clrscr();

 int i,j,index,k,z,t,digits[10];
 long double d,last,n;
 char ch;

 ifstream fi("b.in");
 ofstream fo("cout.in");
 fi>>t;
 fi.get(ch);

 for(i=1;i<=t;i++)
 {
  last=0;
  fi>>n;
  if(n)
  {
   for(z=0;z<10;z++)
   digits[z]=0;

   for(j=1;j<10000;j++)
   {
    last=j*n;
    while(last)
    {
     d=fmod(last,10);
     last=(last-d)/10;
     digits[d]=1;
    }
    last=n*j;
    index=0;
    for(k=0;k<10;k++)
    {
     if(digits[k]==0)
     {index=1; break;}
    }
    if(index==0)
    break;
   }

   fo<<"Case #"<<i<<": "<<last<<"\n";
  }
  else
  {
   fo<<"Case #"<<i<<": INSOMNIA\n";
  }
 }

 fi.close();
 fo.close();

 getch();
}