//cookie
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
double tot_time,time,rate;
int T, ctr=0;;
void solve(float C,float F,float X)
{
ofstream out;
out.open("output.txt",ofstream::out | ofstream::app);

do
 {
 time=C/rate;
 if(time+X/(rate+F)<X/rate)
  {
  tot_time+=time;
  rate+=F;
  }
  else
  {
  tot_time+=X/rate;
  break;
  }
 }
 while(1);
out<<"Case #"<<ctr+1<<": "<<tot_time<<endl;
}
void main()
{
float C,F,X;
clrscr();
ifstream in;
in.open("input.in");
if(!in)
 {
 cout<<"File does not exist";
 getch();
 return;
 }
 in>>T;
   while(ctr!=T){
   in>>C>>F>>X;
   rate=2;tot_time=0;time=0;
   solve(C,F,X);
ctr++;
   }
  getch();
}