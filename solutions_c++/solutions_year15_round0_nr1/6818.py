#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
  ifstream ifile("input.txt", ifstream::in);
  ofstream ofile("output.txt", ifstream::out);
  int tcnt;
  ifile >> tcnt;
  for (int i = 0; i < tcnt; i++)
  {
    int maxsh;
    ifile >> maxsh;
    string ppl;
    ifile >> ppl;
    int pplup = 0;
    int cnt = 0;
    for (int shlvl = 0; pplup < maxsh && shlvl <= maxsh; shlvl++)
    {
      char p = ppl[shlvl];
      if (p == '0') continue;
      if (pplup < shlvl)
      {
        cnt += (shlvl - pplup);
        pplup += (shlvl - pplup);
      }
      pplup += (p - '0');
    }
    ofile << "Case #" << (i+1) << ": " << cnt << endl;
  }
}

