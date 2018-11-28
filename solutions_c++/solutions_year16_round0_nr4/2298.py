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
  uint K, C, S;
  for (int i = 1; i <= T; i++)
  {
	bool found = false;
	input >> K; //tiles
	input >> C; //complexity
	input >> S; //students
	getline(input, line);
#ifdef _DEBUG
//     out << K << endl;
#endif // _DEBUG



	out << "Case #" << i << ": ";
	for (uint pos = 1; pos < K; pos++)
	{
		out << pos << " ";
	}
	out << K << endl;
  }
	return 0;
}

