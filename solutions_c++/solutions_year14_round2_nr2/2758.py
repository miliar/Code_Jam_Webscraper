#include<fstream.h>
#include<conio.h>

int a,b,k,test,cases=1;
float counter=0;

ifstream fin("input.txt");
ofstream fout("output.txt");

void main()
{
 clrscr();

 int i,j;

 fin>>test;

 while(cases<=test)
 {
  counter=0;

  fin>>a;
  fin>>b;
  fin>>k;

  for(i=0;i<a;i++)
  {
   for(j=0;j<b;j++)
   {
    int temp=i&j;

    if(temp<k)
    counter++;
   }
  }

  fout<<"Case #"<<cases<<": "<<counter<<"\n";

  cases++;
 }
 getch();
}