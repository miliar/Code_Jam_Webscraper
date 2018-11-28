#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
  ifstream in(argv[1]);
  unsigned int N;
  in >> N;
  in.ignore();

  for (unsigned int n = 0; n < N; ++n)
  {
    vector<unsigned int> diners;
    unsigned int D, P;
    in >> D;
    diners.reserve(D);
    for (; D > 0; --D)
    {
      in >> P;
      diners.push_back(P);
    }
    sort(diners.begin(), diners.end(), greater<unsigned int>());

//    cout << "Case #"<<n+1<<":";
//    for (auto p : diners)
//      cout << " " << p;

    unsigned int best_time = diners.front();
    unsigned int nr_splits = 0;
    while (diners.front() > 3)
    {
      ++nr_splits;
      auto top = diners.front();
      unsigned int a = top / 2;
      // TODO: large dataset needs more primes
      if (top % 3 == 0 && top % 2 != 0)
      {
        unsigned int next = 0;
        auto it = diners.begin() + 1;
        if (it != diners.end())
          next = *it;
        if (next < top && (next <= top / 3 || next % 3 == 0))
          a = top / 3;
      }
      diners.front() = a;
      diners.push_back(top - a);
      sort(diners.begin(), diners.end(), greater<unsigned int>());

      if (diners.front() + nr_splits < best_time)
      {
        best_time = diners.front() + nr_splits;
      }
    }

    cout << "Case #"<<n+1<<": " << best_time <<endl;
//    cout << " = " << best_time << endl;
  }
}
