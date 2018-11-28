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

int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s,hist;
  int T,t=0;  // number of test cases.
  int n; // number of friends to invite.
  int shy; // current shyness level
  int rshy,tp; // currently required shyness level.
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
      std::getline(in,s); // test case t, S_max S_max+1 digits for all shyness levels.
      buf.str(s);
      buf >> n;
      buf >> hist;
      nf = hist.c_str();
      // count number of 0s in the string, that's pretty much it...
      n=0;
      shy = 0;
      rshy = 0;
      tp=0;
      //printf("case %d\n",t);
      while(nf[rshy])
      {
        // at this level we require rshy, we need to count how many people are *before* this level, if less than required, compensate with n.
        //printf("n: %d shy: %d rshy: %d nf: %d\n",n,shy,rshy,nf[rshy]-48);
        if(shy < rshy)
        {
          n += (rshy - shy);
        }
        tp += (nf[rshy] - 48);
        shy = n + tp;
        rshy++;
      }
      buf.clear();
      out << "Case #" << t << ": " << n << "\n";
    }
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}
