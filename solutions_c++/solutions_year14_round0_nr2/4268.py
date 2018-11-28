#include<iostream>
#include<iomanip>
#include<fstream>
#include<math.h>

using namespace std;

main()
{

 ifstream fin;
 ofstream fout;
 fin.open("B-large.in");
 fout.open("Output.txt");
 long double f,c,x,r=2.0;
 long double a=0,b=0;
 int T,i,j,k;
 fin>>T;
 for(i=0;i<T;i++)
 {
  fin>>c>>f>>x;
  a=x/(2.0);
  for(j=0;j<=(x/c);j++)
  {
   r=2.0;
   b=0;
   for(k=0;k<j;k++)
   {
    b+=(c/r);
    r+=f;
   }
   b+=(x/r);
   if(b<=a)
    a=b;
  }
  int pres=(floor(log10(a)))+8;
  fout.precision(pres);
  fout<<"Case #"<<i+1<<": "<<a<<"\n";
 }
}
