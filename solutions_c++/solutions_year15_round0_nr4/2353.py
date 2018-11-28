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
  int T = 0;
  input >> T ;
  string line;
  getline(input, line); //burn the empty line
  bool Richard = true;
  int X, R, C;
  for (int i = 1; i <= T; i++)
  {
    Richard = true;
    input >> X >> R >> C;
    getline(input, line); 
#ifdef _DEBUG
    out << X << " " << R << " " << C << endl;
#endif // _DEBUG

    switch (X)
    {
    case 1:
      Richard = false;
      break;
    case 2:
      if ((R*C)%2 == 0)
        Richard = false;
      break;
    case 3:
      if (R > 1 && C > 1 && (R*C%3 == 0))
        Richard = false;
      break;
    case 4:
      if (R*C == 16 || R*C == 12)
        Richard = false;
      break;
    default:
      break;
    }
    out << "Case #" << i << ": ";
    if (Richard)
      out << "RICHARD" << endl;
    else
      out << "GABRIEL" << endl;
  }
	return 0;
}

