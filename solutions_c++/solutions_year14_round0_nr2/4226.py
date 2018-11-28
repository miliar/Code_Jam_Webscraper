#include<iostream>
#include<iomanip>
#include<fstream>
#include<string.h>
#include<stdlib.h>
#include<math.h>

using namespace std;

int main()
{

  ifstream fin;
  ofstream fout;
  fin.open("B-large.in");
  fout.open("output2");

  fout.precision(7);

  long double f,c,x,r=2.0;
  long double sol1=0,sol2=0;

  int T,i,j,k;

  fin>>T;

  for(i=0;i<T;i++)
    {

      fin>>c>>f>>x;

      sol1=x/(2.0);

      for(j=0;j<=(x/c);j++)
	{
	  r=2.0;
	  sol2=0;

	  for(k=0;k<j;k++)
	    {
	      sol2+=(c/r);

	      r+=f;
	    }

	  sol2+=(x/r);

	  if(sol2<=sol1)
	    {sol1=sol2;}
	}

      int pres=(floor(log10(sol1)))+8;
      fout.precision(pres);
      fout<<"Case #"<<i+1<<": "<<sol1<<"\n";
      
    }

}
