#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <math.h>
//#include <cstdint>
#include <iomanip>
typedef unsigned long long uint;
using namespace std;

void flip(string& pancakes, string control, uint flipPos, uint& numFlips)
{
	while (pancakes != control)
	{
		if (flipPos + 1 < pancakes.size() && pancakes[flipPos] == pancakes[flipPos + 1])
			flip(pancakes, control, flipPos + 1, numFlips);
		else
		{
			numFlips++;
			for (uint pos = 0; pos <= flipPos; pos++)
			{
				pancakes[pos] = (pancakes[pos] == '-') ? '+' : '-';
			}

		}
		flipPos = 0;
	}
}

//typedef unsigned int uint;

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int T = 0;
  input >> T ;
  string line;
  getline(input, line); //burn the empty line
  for (int i = 1; i <= T; i++)
  {
	uint flips = 0;
	string pancakes;
	input >> pancakes; 
	string control(pancakes.size(), '+');
	getline(input, line);
#ifdef _DEBUG
//     out << K << endl;
#endif // _DEBUG

	flip(pancakes, control, 0, flips);
	out << "Case #" << i << ": " << flips << endl;
  }
	return 0;
}

