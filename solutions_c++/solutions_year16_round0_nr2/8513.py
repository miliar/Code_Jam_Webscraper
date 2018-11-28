#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>

void main()
{
 clrscr();

 int t,i,j,len,one,two,count;
 char ch, str[110];

 ifstream fi("b.in");
 ofstream fo("cout.in");
 fi>>t;
 fi.get(ch);

 for(i=1;i<=t;i++)
 {
  count=0;
  fi>>str;
  fi.get(ch);
  len=strlen(str);
  for(j=1;j<len;j++)
  {
   one=str[j-1];
   two=str[j];
   if(one!=two)
   count+=1;
  }
  if(str[len-1]!='+')
  count+=1;

  fo<<"Case #"<<i<<": "<<count<<"\n";
 }

 fi.close();
 fo.close();

 getch();
}