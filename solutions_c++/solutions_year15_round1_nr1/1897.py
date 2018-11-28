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
  int N;
  int shrooms[1002];
  for (int i = 1; i <= T; i++)
  {
    input >> N;
    getline(input, line); 
#ifdef _DEBUG
//    out << N << " " << R << " " << C << endl;
#endif // _DEBUG

    int MinMushA = 0;
    int MinMushB = 0;
    int MaxRateB = 0;
    int lastCount = 0;
    for (int j = 0; j < N; j++)
    {
      int count = 0;
      input >> count;
      shrooms[j] = count;
      if (j > 0)
      {
        int diff = lastCount - count;
        if (diff > 0)
        {
          MinMushA += diff;
          if (diff > MaxRateB)
            MaxRateB = diff;
        }
      }
      lastCount = count;
    }
    for (int j = 0; j < N-1; j++)
    {
      if (MaxRateB > shrooms[j])
        MinMushB += shrooms[j];
      else
        MinMushB += MaxRateB;
    }
    out << "Case #" << i << ": " << MinMushA << " " << MinMushB << endl;
  }
	return 0;
}

