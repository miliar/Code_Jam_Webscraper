#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <math.h>
//#include <cstdint>
#include <iomanip>
#include <bitset>
typedef unsigned long long uint;
using namespace std;

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int T = 0;
  input >> T ;
  string line;
  getline(input, line); //burn the empty line
  string nums[] =
  {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
  };

  for (int i = 1; i <= T; i++)
  {
	  string scrambled;
    stringstream unscrambled;
	  input >> scrambled;
	  getline(input, line);
    string fresh = scrambled;
    int countZero, countTwo, countSix, countEight, counts[10];
    memset(counts,0,sizeof(counts));

    counts[0] = countZero = std::count(scrambled.begin(), scrambled.end(), 'Z');
    counts[2] = countTwo = std::count(scrambled.begin(), scrambled.end(), 'W');
    counts[6] = countSix = std::count(scrambled.begin(), scrambled.end(), 'X');
    counts[8] = countEight = std::count(scrambled.begin(), scrambled.end(), 'G');
    counts[3] = std::count(scrambled.begin(), scrambled.end(), 'T') - countEight - countTwo;
    counts[7] = std::count(scrambled.begin(), scrambled.end(), 'S') - countSix;
    counts[5] = std::count(scrambled.begin(), scrambled.end(), 'V') - counts[7];
    counts[4] = std::count(scrambled.begin(), scrambled.end(), 'F') - counts[5];
    counts[1] = std::count(scrambled.begin(), scrambled.end(), 'O') - counts[4] - countZero - countTwo;
    counts[9] = std::count(scrambled.begin(), scrambled.end(), 'I') - counts[5] - countSix - countEight;

    for (int j = 0; j<10; j++)
    {
      for (int k=0; k<counts[j];k++)
      {
        unscrambled << j;
      }
    }

    out << "Case #" << i << ": " << unscrambled.str() << endl;
  }
	return 0;
}

