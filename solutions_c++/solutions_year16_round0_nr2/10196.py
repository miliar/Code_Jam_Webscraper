#include<fstream.h>
#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<graphics.h>
#include<dos.h>
#include<ctype.h>
#include<process.h>
ofstream out;
ifstream in;
void main()
{
clrscr();
void flip(int a[],int in);
int a[10],len,z=0,re=0,tep,t;
 char ch[10],d[10];
cout<<"Enter test cases ";cin>>t;
out.open("j1sf.txt",ios::app);
out<<"Input"<<"        "<<"output"<<endl;
out<<t<<endl;
out.close();
 in.open("j1if.txt",ios::in);
 out.open("j1sf.txt",ios::app);
 for(int f=1;f<=t;f++)
 {
   re=0;
   in>>d;
   cout<<"Character input "<<d<<endl;
   strcpy(ch,d);
  len=strlen(ch);
   for(int i=0;i<len;i++)
    {
     a[i]=(ch[i]*1)-48;
      if(a[i]==-5) a[i]=1;
      if(a[i]==-3) a[i]=0;
    }
   int k=0;
   tep=a[0];

   do
    {
     z=0;
      for(int j=0;j<len;j++)
       {
         if(a[j]==0) z=1;
       }
      if(z==0) break;
      if(a[len-1]==0 && a[0]==0)
       {
        int l=len-1;
         flip(a,l);
         re++;
         k=-1;
         tep=a[0];
       }
       else
       {
        if(a[k]!=tep)
         {
         int g;
          g=k-1;
          flip(a,g);
          tep=a[0];
          k=-1;
          re++;
         }
       }
    k++;
    }while(z==1);
  cout<<"Result output "<<re<<endl;
  out<<d<<"       "<<"Case #"<<f<<": "<<re<<endl;
  getch();
 }
in.close();
out.close();
getch();
}
void flip(int a[],int in)
 {
  int tep,l=in;
  for(int j=0;j<=in;j++)
   {
    if(a[j]==1)
    a[j]=0;
    else if(a[j]==0)
    a[j]=1;
   }
   for(int i=0;i<=in/2;i++,l--)
    {
     tep=a[i];
     a[i]=a[l];
     a[l]=tep;
    }
  getch();
  clrscr();
 }