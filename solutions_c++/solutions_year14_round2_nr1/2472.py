#include<stdio.h>
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<iomanip.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

int result,max,flength,slength,n,cases;
char array[2][101];

char ch;

void main()
 {
  clrscr();
  int i,j,k,m=0,l=0;
  ifstream filin;
  filin.open("googin.in",ios::in);
  ofstream filout;
  filout.open("googout.in",ios::out);
  filin>>cases;
  filin.get(ch);
  for (i=0;i<cases;i++)
   {
    m=0;
    l=0;
    result=0;
    filin>>n;
    filin.get(ch);
      for(k=0;;k++)
       {
	filin>>array[0];
	break;
       }
      flength=strlen(array[0]);
      for (k=0;;k++)
       {
	filin>>array[1];
	  break;
       }
      slength=strlen(array[1]);
    if (flength>slength)
      max=flength;
    else
      max=slength;
    if (array[0][0]==array[1][0]);
    else
     {
      result=-1;
      goto end;
     }
    for (k=0;(((k+m)<flength)&&((k+l)<slength));)
     {
      if (array[0][k+m]==array[1][k+l])
       {
	if ((k+1+m==flength)&&(k+1+l!=slength))
	 {
	  result++;
	  l++;
	 }
	if ((k+1+m!=flength)&&(k+1+l==slength))
	 {
	  result++;
	  m++;
	 }
	if ((k+1+m==flength)&&(k+1+l==slength))
	 {
	  goto end;
	 }
	if ((k+1+m!=flength)&&(k+1+l!=slength))
	  k++;
       }
      else
       {
	if (array[0][k+m]==array[0][k+m-1])
	 {
	  result++;
	  m++;
	  goto loopend;
	 }
	if (array[1][k+l]==array[1][k+l-1])
	 {
	  result++;
	  l++;
	  goto loopend;
	 }
	if ((array[0][k+m]!=array[0][k+m-1])&&(array[1][k+l]!=array[1][k+l-1]))
	 {
	  result=-1;
	  goto end;
	 }
       }
      loopend:
     }
    end:
    if (array[0][flength-1]!=array[1][slength-1])
      result=-1;
    if (result==-1)
      filout<<"Case #"<<i+1<<": "<<"Fegla Won"<<'\n';
    else
      filout<<"Case #"<<i+1<<": "<<result<<'\n';
   }
  filin.close();
  filout.close();
  getch();
 }