#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<iomanip.h>


ifstream fin("abc.txt");
ofstream fout("ans.txt");

double F,X,C;

void calc_time(int cse)
{
 double rate=2,time=0;
 double temp1,temp2;
 temp1=X/rate;
 temp2=(C/rate)+(X/(rate+F));
 while(temp2<temp1)
 {
  time=time+(C/rate);
  rate=rate+F;
  temp1=X/rate;
  temp2=(C/rate)+(X/(rate+F));
 }
 time=time+(X/rate);
 fout<<"Case #"<<cse+1<<": "<<time<<"\n";
}

void main()
{
 clrscr();
 int total=0;
 fin>>total;
 for(int i=0;i<total;i++)
 {
  fin>>C;
  fin>>F;
  fin>>X;
  calc_time(i);
 }
 getch();
}
