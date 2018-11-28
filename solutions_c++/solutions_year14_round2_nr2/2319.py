#include<stdio.h>
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<iomanip.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

long int count=0,cases,a,b,k;

char ch;

void main()
 {
  clrscr();
  int i,j,l;
  ifstream filin;
  filin.open("googin.in",ios::in);
  ofstream filout;
  filout.open("googout.in",ios::out);
  filin>>cases;
  filin.get(ch);
  for (i=0;i<cases;i++)
   {
    count=0;
    filin>>a;
    filin.get(ch);
    filin>>b;
    filin.get(ch);
    filin>>k;
    filin.get(ch);
    for (j=0;j<a;j++)
     {
      for (l=0;l<b;l++)
       {
	if ((j&l)<k)
	 {
	  count++;
	 }
       }
     }
    filout<<"Case #"<<i+1<<": "<<count<<'\n';
   }
  filin.close();
  filout.close();
  getch();
 }