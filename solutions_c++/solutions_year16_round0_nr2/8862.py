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
#include <map>
#include <stdlib.h>

int happy_pancakes(const char *stack);

int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s;
  int T,t=0;  // number of test cases.
  const char *p_stack;
  
  const char *nf;
  if(argc==2)
  {
    in.open(argv[1]);
    out.open((std::string(argv[1]) + ".out").c_str(),std::ofstream::out|std::ofstream::trunc);
    std::getline(in,s);  // number of test cases
    buf.str(s);
    buf >> T;  // T test cases
    buf.clear();
    while(t<T)
    {
      t++;
      std::getline(in,s);
      p_stack = s.c_str();
      out << "Case #" << t << ": " << happy_pancakes(p_stack) << "\n";
    }
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}

int happy_pancakes(const char *stack)
{
      char work;
      int n_flips;
      // de-duplicate the string, compress it.
      work=stack[0];
      for(int i=1;stack[i];i++)
      {
        if(work != stack[i])
        {
          // change detected, we will do two things
          // one, lets do the flip right here, then we make our work char the current char.
          work = stack[i]; // yes, this flips it :P
          n_flips++;
        }
      }
      // end of string, last char?
      if(work == '-')
        n_flips++; // one extra flip.
      return n_flips;
}