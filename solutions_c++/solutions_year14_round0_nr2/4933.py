#include<iomanip.h>
#include<iostream.h>
#include<fstream.h>
#include<conio.h>

long double results(void);

long double result[100];

long double c,f,x;

void main()
 {
  int cases,i;
  char junk;
  clrscr();
  ifstream filin;
  filin.open("goog2i.in",ios::in);
  filin>>cases;
  filin.get(junk);
  for (i=0;i<cases;i++)
   {
    filin>>c;
    filin.get(junk);
    filin>>f;
    filin.get(junk);
    filin>>x;
    filin.get(junk);
    result[i]=results();
   }
  filin.close();
  ofstream filout;
  filout.open("goog2o.in",ios::out);
  for (i=0;i<cases;i++)
   {
    filout<<"Case #"<<i+1<<": ";
    filout.setf(ios::fixed);
    filout.setf(ios::showpoint);
    filout<<result[i]<<'\n';
   }
  filout.close();
 }

long double results(void)
 {
  long double t,temp=(long double)(x/2.0);
  int n,i;
  for (n=0;;n++)
   {
    t=0.0;
    for  (i=0;i<n;i++)
      t+=(long double)(c/(2.0+(((long double)i)*f)));
    t+=(long double)(x/(2.0+(((long double)n)*f)));
    if (t<=temp)
      temp=t;
    else
      return temp;
   }
 }