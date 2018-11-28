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
  std::string s;
  int T,t=0;  // number of test cases.
  int64_t N; // given number
  int64_t last_named; // last named number
  char n[12];
  
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
      buf.str(s);
      buf >> N;
      buf.clear();
      if(N==0)
      {
        out << "Case #" << t << ": INSOMNIA\n";
//        std::cout << "Case #" << t << ": INSOMNIA\n";
        continue;
      }
      else
      {
        int seen=0; // bitmask for the seen integers, once we see them all (0 to 9), so, 11 1111 1111=0x1FF, we are done.
        int64_t x=1;
        
        while(seen ^ 0x3FF)
        {
  //        std::cout << "Case #" << t << ": " << "processing N " << N << " with x " << x << " seen: " << seen << "\n";
          snprintf(n,12,"%li",last_named=x*N);
          for(int i=0;n[i];i++)
          {
            seen |= (1 << (n[i] - '0'));
          }
          x++;
        }
      }
      
      out << "Case #" << t << ": " << last_named << "\n";
    }
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}
