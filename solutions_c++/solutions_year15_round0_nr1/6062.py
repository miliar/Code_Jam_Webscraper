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
  fin.open("A-large.in");
  fout.open("output1L");

  int i,j,c,T;
  int inv,smax,standing;
  c=(int)('0');

  // fout.precision(7);
  
  fin>>T;
  
  for(i=0;i<T;i++)
    {      
      fin>>smax;
      char arr[smax+1];
      fin>>arr;

      standing=(int)(arr[0])-c;
      inv=0;

      for(j=1;j<=smax;j++)
	{
	  if((standing<j)&&(arr[j]!=0))
	    {
	      inv+=(j-standing);
	      standing+=(j-standing);
	    }
	  standing+=(int)(arr[j])-c;
	}
      
      fout<<"Case #"<<i+1<<": "<<inv<<"\n";
  
    }  

}
