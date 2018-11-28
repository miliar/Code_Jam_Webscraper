#include <iostream.h>
#include <conio.h>
#include <fstream.h>
void main()
{
clrscr();
cout<<"\n";
int loops;
ifstream input("input123.in", ios::in);
ofstream output("Arvind1.in", ios::out);
input>>loops;
for (int i=0; i<loops; ++i)
{
double cookiesneeded;
double perfarm;
double time=0;
double rate=2;
double rateinc;
input>>perfarm;
input>>rateinc;
input>>cookiesneeded;
while ((cookiesneeded/rate)>(perfarm/rate)+(cookiesneeded/(rate+rateinc)))
{
time+=perfarm/rate;
rate+=rateinc;
}
time+=cookiesneeded/rate;
output<<"Case #"<<i+1<<": "<<time<<"\n";
}
input.close();
output.close();
cout<<"Success!";
getch();
}


