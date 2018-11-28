
#include <iostream>
#include <fstream>
using namespace std;

string solve(string& s, int S, int E)
{
  char c = 0;
  int idx = -1;
  if (E <= S) return "";
  for (int i = S; i < E; i++)
  {
    if (s[i] > c)
    {
      c = s[i];
      idx = i;
    }
  }
  string mid = solve(s, S, idx);
  string res = s[idx] + mid;
  for (int i = idx+1; i < E; i++)
  {
    if (s[i] == s[idx]) res = s[idx] + res;
    else res = res + s[i];
  }
  return res;
}

void run(istream& in, ostream& out)
{
  int T; in >> T;
  for (int t = 1; t <= T; t++)
  {
    string s; in >> s;
    string res = solve(s, 0, s.size());
    out << "Case #" << t << ": " << res << endl;
  }
}

int main()
{
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  run(fin, fout);
}

