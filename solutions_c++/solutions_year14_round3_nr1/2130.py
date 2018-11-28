#include <string>
#include <iostream>
//#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <ios>
#include <vector>
#include <string.h>
//#include <algorithm>
//#include <map>

int count_1s(long long int a)
{
  int x,c=0;
  for(x=0;x<40;x++) // per problem limits, up to 40 bits.
  {
    if(a & ((long long int)1L)<<x)
      c++;
  }
  return c;
}

void simplify(long long int *P,long long int *G)
{
  long long int x,y;
  x=*P;
  y=*G;
  while(!(x & 0x1) && !(y & 0x1))
  {
    x=x>>1;
    y=y>>1;
  }
  // Now, lets try to simplify using the value of P  (x):
  if(!(y % x))
  {
    y=y/x;
    x=1;
  }
  *P=x;
  *G=y;
}

int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s;
  int T,t=0;  // number of test cases.
  long long int P,G;
  int ng;
  char x;
  if(argc==2)
  {
    in.open(argv[1]);
    out.open((std::string(argv[1]) + ".out").c_str(),std::ofstream::out|std::ofstream::trunc);
    std::getline(in,s); // number of test cases.
    buf.str(s);
    buf >> T;
    buf.clear();
    while(t<T)
    {
      t++;
      ng=0;
      out << "Case #" << t << ": ";
      
      std::getline(in,s);
      buf.str(s);
      // read buf thing
      // buf >> var;
      buf >> P;
      buf >> x;
      buf >> G;
      //std::cout << P << " " << G << std::endl;
      buf.clear();
      x=1;
      simplify(&P,&G);
      if(G & 0x1 || P>G)
      {
	out << "impossible" << std::endl;
      }
      else
      {
	if(P==G)
	{
	  out << 1 << std::endl;
	}
	else
	{
	  if(count_1s(G) > 1)
	  {
	    // not a power of 2
	    if(G % P || P==1)
	    {
	      out << "impossible" << std::endl;
	      x=0;
	    }
	  }
	  if(x)
	  {
	    while(G>P && !(G & 0x1))
	    {
	      ng++;
	      G = G>>1;
	    }
	    out << ng << std::endl;
	  }
	}
      }
    }
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}
