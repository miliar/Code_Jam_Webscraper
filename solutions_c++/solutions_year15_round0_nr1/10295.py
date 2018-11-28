#include <iostream>
#include <string>
#include <math.h>
#include <deque>
#include <algorithm>
#include <map>
#include <vector>
#include <fstream>

using namespace std;

const int maxSmax = 1000;

int main(void)
{
  ifstream in("input.txt");
  ofstream out("output.txt");
  int T = 0;
  
  in >> T;
  for (int i = 0; i < T; i++)
  {
    int smax = 0;
    int sum = 0;
    int extra = 0;
    in >> smax;
    
    in.get();
    for (int j = 0; j < smax + 1; j++)
    {
      char num = in.get() - '0';

      if (num > 0 && j > sum)
      {
        extra += (j - sum);
        sum += (j - sum);
      }

      sum += num;
    }

    out << "Case #" << i + 1 << ": " << extra << endl;
  }

  return 0;
}