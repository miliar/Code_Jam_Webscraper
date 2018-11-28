// MinesweeperMaster.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <math.h>
using namespace std;

int ComputeGenerations(const unsigned __int64 P, const unsigned __int64 Q)
{
  int i = 0;
//  unsigned __int64 A, B, C, D;
  //    if ((A / B + C / D) / 2 == P / Q)

  for (; i < 40; i++)
  {
    unsigned __int64 denominator = (1 << i);
    unsigned __int64 numerator = P * denominator;

    if ((((numerator / Q)) == 1) && (numerator%Q == 0))
      break;

    if (Q == denominator)
    {
      for (int j = 1; j <= i; j++)
      {
        if (P > (Q / (1 << j)))
          return j;
      }

      for (unsigned __int64 j = 0; j < denominator; j++)
      {
        for (unsigned __int64 k = 0; k < denominator; k++)
        {
          if (j + k == P)
            return i;
        }
      }
    }

    if ((Q % 2 << i) == 0)
    {
    }
//     if ((P >(Q / 2 << i)) && ((Q % 2 << i) == 0))
//       return i + 1;

//     if (i == 1)
//     {
//       if (P == 1 && Q == 2)
//         return i;
//     }
//     else if (i == 2)
//     {
//       if ((P == 5 && Q == 8) || (P == 1 && Q == 4))
//         return i;
//     }
//     else if (i == 3)
//     {
//       if (P == 5 && Q == 16)
//         return i;
//     }
  }
  
  if (i<40)
    return i;
  
  return -1;
}

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int T = 0;
  input >> T;
  string line;
  getline(input, line); //burn the empty line
  for (int X = 1; X <= T; X++)
  {
    
    unsigned __int64 P, Q;
    input >> P;
    char slash;
    input >> slash;
    input >> Q;
    getline(input, line); //burn the empty line

    int generations = ComputeGenerations(P, Q);

    out << "Case #" << X << ": ";
    if (generations >= 0)
      out << generations << endl;
    else
      out << "impossible" << endl;
  }
	return 0;
}

