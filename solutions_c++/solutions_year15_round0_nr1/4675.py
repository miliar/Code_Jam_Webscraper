#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <math.h>
//#include <cstdint>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int N = 0;
  input >> N ;
  string line;
  getline(input, line); //burn the empty line
  int people;
  int max;
  char count;
  int required = 0;
  int standing = 0;
  for (int i = 1; i <= N; i++)
  {
    input >> max;
    required = 0;
    standing = 0;
    for (int j = 0; j <= max; j++)
    {
      input >> count;
      people = count - 48;
      if (people && (standing + required < j))
        required += j - (standing + required);

      standing += people;
    }
    getline(input, line); //burn the empty line

    out << "Case #" << i << ": " << required << endl;
  }
	return 0;
}

