#include<fstream.h>
#include<conio.h>
#include<string.h>

int n,num;
char str[100];

void count(int start, int end)
{
 int con=0;
 for(int i=start;i<=end;i++)
 {
  if(str[i]!='a' && str[i]!='e' && str[i]!='i' && str[i]!='o' && str[i]!='u')
  {
   con++;

   if(con==n)
   {
    num++;
    break;
   }
  }
  else
  con=0;
 }
}

void combo()
{
 int e=n,l=strlen(str),j;

 while(e<=l)
 {
  for(j=0;j<l;j++)
  {
   if(e+j>l)
   break;

   count(j,e+j-1);
  }
  e++;
 }
}




void main()
{
 clrscr();
 int k=1,test;

 ifstream fin("A.txt");
 ofstream fout("Out.txt");

 fin>>test;

 while(k<=test)
 {
  num=0;

  fin>>str;
  fin>>n;

  combo();
  fout<<"Case #"<<k<<": "<<num<<"\n";

  k++;
 }
 getch();
}