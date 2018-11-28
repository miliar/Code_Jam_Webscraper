#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
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
  int D = 0;
  int next = 0;
  int minutes = 0;
  int count = 0;
  map <int,int> P;
  input >> T;
  string line;
  bool found = false;
  getline(input, line); //burn the empty line
  int maxP = 0;
  for (int i = 1; i <= T; i++)
  {
    input >> D;
    getline(input, line); //burn the empty line
    minutes = 0;
    P.clear();
    maxP = 0;

    for (int j = 0; j < D; j++)
    {
      input >> next;
#ifdef _DEBUG
      out << next << " ";
#endif // DEBUG
      P[next]++;
    }
#ifdef _DEBUG
    out << endl;
#endif // DEBUG

    for (auto j:P)
    {
      if (j.first > maxP)
        maxP = j.first;
    }
    found = false;

    for (int j = maxP; j >= 0 && !found; j--)
    {
      count = 0;
      int half = j / 2;
      bool first = true;
      while (P[j] && !found)
      {
        if (j == 9) 
        {
          if (first)
          {
            first = false;
            int count4to8 = P[4] + P[5] + P[6] + P[7] + P[8];
            if ((P[j] == 1) && !(count4to8 > 1))
            {
              P[j]--;
              P[6]++;
              P[3]++;
              minutes++;
              break;
            }
          }
        }
        if (j + minutes < maxP)
          maxP = j + minutes;
        count = P[j] - 1;
        for (int k = half; k<j && P[j]; k++)
        {
          count += P[k];
          if (count >= half && (P[k] && k + 1 > j))
          {
            minutes += j;
            found = true;
            break;
          }
        }
        if (found)
          break;
        else if (j < 4)
        {
          if (P[j])
          {
            minutes += j;
            found = true;
            break;
          }
        }
        else
        {
          minutes++;
          P[j]--;
          P[half]++;
          if (j%2)
            P[half+1]++;
          else
            P[half]++;
        }
      }
    }

    if (minutes > maxP)
      minutes = maxP;
    out << "Case #" << i << ": ";
    out << minutes << endl;
  }
	return 0;
}

