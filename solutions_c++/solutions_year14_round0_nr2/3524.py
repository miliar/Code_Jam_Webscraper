#include<fstream.h>
#include<conio.h>

double farmcost,farmrate,rate=2,target;
int counter=1;

ifstream fin("input.txt");
ofstream fout("output.txt");

void minimum_time()
{
 double time=target/rate;

 double farmtime,temptime,prevfarmtimes=0;

 do
 {
   farmtime=farmcost/rate;

   temptime=prevfarmtimes+farmtime+(target/(rate+farmrate));

   if(temptime<time)
   {
    time=temptime;
    rate=rate+farmrate;
    prevfarmtimes=prevfarmtimes+farmtime;
   }
   else
   break;
 }while(1);

 fout<<"Case #"<<counter<<": "<<time<<"\n";
}

void main()
{
 clrscr();

 int test;

 fin>>test;

 while(counter<=test)
 {
  fin>>farmcost;
  fin>>farmrate;
  fin>>target;

  rate=2;

  minimum_time();

  counter++;
 }

 getch();
}