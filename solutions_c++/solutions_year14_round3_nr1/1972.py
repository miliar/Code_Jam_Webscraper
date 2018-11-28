#include<stdio.h>
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<iomanip.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

int cases;

char ch;

void main()
 {
  clrscr();
  int i,j,k;
  long int one,denom,a,b,count;
  ifstream filin;
  filin.open("googin.in",ios::in);
  ofstream filout;
  filout.open("googout.in",ios::out);
  filin>>cases;
  filin.get(ch);
  for (i=0;i<cases;i++)
   {
    one=1;
    filin>>a;
    filin>>ch;
    filin>>b;
    filin.get(ch);
    /*
    for (j=2;;)
     {
      if ((a<j)||((a==j)&&(a%b!=0)))
       {
       break;
       }
       {
      if (a%j==0&&b%j==0)
       {
	a/=j;
	b/=j;
       }
      else
	j++;
      }
     } */
    for (j=2;(a>=j)&&((a==j)||(a%b!=0));)
     {
      if (a%j==0&&b%j==0)
       {
	a/=j;
	b/=j;
       }
      else
	j++;
     }
    for (j=0;one<b;j++)
     {
      one*=2;
     }
    if (pow(2,j)==one)
     {
     for (count=0;;count++)
    {
     a*=2;
     if (a>=b)
       break;
    }
    filout<<"Case #"<<i+1<<": "<<count+1<<'\n';
      /*for (count=0;a!=b;count++)
      {
      if (((a-1)%4==0)&&(a!=1))
       {
	a=a-1;
	for (j=2;j!=3;)
	 {
	  if (a%j==0&&b%j==0)
	   {
	    a/=j;
	    b/=j;
	   }
	  else
	    j++;
	 }
       }
      else
       {
	a=a+1;
	for (j=2;j!=3;)
	 {
	  if (a%j==0&&b%j==0)
	   {
	    a/=j;
	    b/=j;
	   }
	  else
	    j++;
	 }
       }
     }
      filout<<"Case #"<<i+1<<": "<<count<<'\n';    */
     }
    else
     {
      filout<<"Case #"<<i+1<<": "<<"impossible"<<'\n';
     }
    cout<<i+1<<" ";
   for (count=0;;count++)
    {
     a*=2;
     if (a>=b)
       break;
    }

   }
  filin.close();
  filout.close();
  getch();
 }