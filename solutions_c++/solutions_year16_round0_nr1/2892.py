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
//typedef unsigned int uint;
using namespace std;

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int T = 0;
  input >> T ;
  string line;
  getline(input, line); //burn the empty line
  uint N;
  char testDigits[10];
  memset(testDigits, 1, 10);
  for (int i = 1; i <= T; i++)
  {
	bool found = false;
	input >> N;
	getline(input, line);
#ifdef _DEBUG
//     out << N << endl;
#endif // _DEBUG


	char digits[10];
	memset(digits, 0, 10);

	uint said = N;
	std::stringstream  ss;
	ss << said;

	if (N > 0)
	{
		for (uint tries = 0; tries < ULLONG_MAX; tries++)
		{
			for (int j = 0; j < ss.str().size(); j++)
			{
				int val = ss.str()[j] - 48;
				digits[val] = 1;

				if (memcmp(digits, testDigits, 10) == 0)
				{
					found = true;
					break;
				}
			}

			if (found)
				break;
			else
			{
				said = (tries + 1) * N;
				ss << said;
			}
		}
	}

	out << "Case #" << i << ": ";
	if (found)
		out << said << endl;
	else
		out << "INSOMNIA" << endl;
  }
	return 0;
}

