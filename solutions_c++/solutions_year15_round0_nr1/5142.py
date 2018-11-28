#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T;
int Smax;
vector<int> S;

string input = "A-small-attempt1.in";
string output = "A-small-attempt1.out";

int main()
{
  ifstream fin(input);
  ofstream fout(output);
  fin >> T;
  for (auto t = 1; t <= T; ++t)
  {
    fin >> Smax;
    S.resize(Smax + 1);
    fin.get();
    for (int i = 0; i <= Smax; ++i)
    {
      S[i] = fin.get() - '0';
    }
    int friends = 0;
    int stands = 0;
    for (int i = 0; i <= Smax; ++i)
    {
      if (stands < i && S[i] > 0)
      {
        friends += i - stands;
        stands += friends + S[i];
      }
      else
      {
        stands += S[i];
      }
    }
    fout << "Case #" << t << ": " << friends << endl;
  }
}