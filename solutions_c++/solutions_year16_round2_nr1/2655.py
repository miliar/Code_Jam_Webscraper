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

char *insert(char c, char *word);
char *append(char c, char *word);

/*
 * 1<=T<=100
 * 
 * 3<=len S<=20
 * 3<=len S<=2000
 * 
 * S=string.
 * 
 * Read each character, increase its corresponding counter.
 * 
"ZERO"  Z
"ONE" 
"TWO"   W
"THREE"
"FOUR"   U
"FIVE"
"SIX"   X
"SEVEN"
"EIGHT"  G
"NINE"
 * 
 * Fixed options:
 * We have Z=0, remove Z E R O
 * W=2, remove T W O
 * U=4, remove F O U R
 * X=6, remove S I X
 * G=8, remove E I G H T
 *  After that, we have:
"ONE"     O=1, remove O N E
"THREE"   T=3, remove T H R EE
"FIVE"    F=5, remove F I V E
"SEVEN"   S=7, remove S E V E N
* After that: 
"NINE"    N=9, remove N I N E
 */
int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s;
  int T,t=0;  // number of test cases.
  const char *word;
  int az[27];
  int digits[10];
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
      memset(az,0,27*sizeof(int));
      memset(digits,0,10*sizeof(int));
      t++;
      std::cout << "case " << t << "\n";
      std::getline(in,s);
      word=s.c_str();
      std::cout << word << "\n";
      // Create the "histogram"
      for(int i=0;word[i];i++)
      {
        az[word[i]-'A']++;
      }
      // ZERO Z Z0,W2,U4,X6,G8
      int d=0;
      while(az['Z'-'A'])
      {
        digits[0]++;
        az['Z'-'A']--;
        az['E'-'A']--;
        az['R'-'A']--;
        az['O'-'A']--;
      }
      // TWO W
      std::cout << "TWO" << "\n";
      while(az['W'-'A'])
      {
        digits[2]++;
        az['T'-'A']--;
        az['W'-'A']--;
        az['O'-'A']--;
      }
      // FOUR U
      std::cout << "FOUR" << "\n";
      while(az['U'-'A'])
      {
        digits[4]++;
        az['F'-'A']--;
        az['O'-'A']--;
        az['U'-'A']--;
        az['R'-'A']--;
      }
      // SIX X
      std::cout << "SIX\n";
      while(az['X'-'A'])
      {
        digits[6]++;
        az['S'-'A']--;
        az['I'-'A']--;
        az['X'-'A']--;
      }
      // EIGHT G
      std::cout << "EIGHT\n";
      while(az['G'-'A'])
      {
        digits[8]++;
        az['E'-'A']--;
        az['I'-'A']--;
        az['G'-'A']--;
        az['H'-'A']--;
        az['T'-'A']--;
      }
/*
 * "ONE"     O=1, remove O N E
"THREE"   T=3, remove T H R EE
"FIVE"    F=5, remove F I V E
"SEVEN"   S=7, remove S E V E N
* After that: 
"NINE"    N=9, remove N I N E
*/
      // ONE O
      std::cout << "ONE\n";
      while(az['O'-'A'])
      {
        digits[1]++;
        az['O'-'A']--;
        az['N'-'A']--;
        az['E'-'A']--;
      }
      // THREE T
      while(az['T'-'A'])
      {
        digits[3]++;
        az['T'-'A']--;
        az['H'-'A']--;
        az['R'-'A']--;
        az['E'-'A']--;
        az['E'-'A']--;
      }
      // FIVE F
      while(az['F'-'A'])
      {
        digits[5]++;
        az['F'-'A']--;
        az['I'-'A']--;
        az['V'-'A']--;
        az['E'-'A']--;
      }
      // SEVEN S
      while(az['S'-'A'])
      {
        digits[7]++;
        az['S'-'A']--;
        az['E'-'A']--;
        az['V'-'A']--;
        az['E'-'A']--;
        az['N'-'A']--;
      }
      // NINE N
      while(az['N'-'A'])
      {
        digits[9]++;
        az['N'-'A']--;
        az['I'-'A']--;
        az['N'-'A']--;
        az['E'-'A']--;
      }
      std::cout << "print case#\n";
      out << "Case #" << t << ": ";
      for(int i=0;i<10;i++)
      {
//        std::cout << i << ": " << digits[i] << "\n";
        while(digits[i])
        {
          out << i;
          digits[i]--;
        }
      }
      out << "\n";
    }
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}

