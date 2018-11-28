#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int T;
int D;
vector<int> A;
vector<int> B;
vector<int> answers;

//string input = "B-sample.in";
//string output = "B-sample.out";
//string input = "B-small-attempt2.in";
//string output = "B-small-attempt2.out";
string input = "B-large.in";
string output = "B-large.out";

int main()
{
  ifstream fin(input);
  ofstream fout(output);
  fin >> T;
  for (auto t = 1; t <= T; ++t)
  {
    A.resize(1001, 0);
    answers.clear();
    fin >> D;
    int maxPi = 0;
    for (int d = 0; d < D; ++d)
    {
      int Pi;
      fin >> A[d];
      if (A[d] > maxPi)
      {
        maxPi = A[d];
      }
    }
    int minute = maxPi;
    int special = 0;
    answers.push_back(minute);
    for (int k = 0; k < maxPi; ++k)
    {
      // find the minimum maximum value achievable for k splits
      for (int m = maxPi; m > 0; --m)
      {
        // can we achieve a maximum of m?
        int splits = 0;
        for (int i = 0; i < D; ++i)
        {
          int temp = A[i];
          while (temp > m)
          {
            temp -= m;
            ++splits;
            if (splits > k) break;
          }
        }
        if (splits <= k)
        {
          answers.push_back(m + k);
        }
        else
        {
          break;
        }
      }
    }
    fout << "Case #" << t << ": " << *min_element(answers.begin(), answers.end()) << endl;
  }
}