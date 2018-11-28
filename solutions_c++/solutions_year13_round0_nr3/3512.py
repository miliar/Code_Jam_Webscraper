#include<fstream>
#include<iostream>
#include<vector>
#include <limits>
#include<algorithm>
#include <functional>
#include<cmath>
#include<xstring>
#include<string>
using namespace std;
int main()
  {
  int T;
  ifstream f("C-small-attempt1.in");
  ofstream g("output.txt");
  f >> T;
  string num;
  vector<__int64> res(T);
  string a;
  __int64 A, B;
  long double C;
  for(int i = 0 ; i < T ; ++i)
    {
    f >> A >> B;
    __int64 counter = 0;
    for(__int64 j = A; j <= B; ++j)
      {
        a = to_string(j);
        bool ispal = true;
        int asize = a.size();
        for(int k = 0 ; k < asize / 2; ++k)
          if(a[k] != a[asize - 1 - k])
            {
            ispal = false;
            break;
            }
        if(ispal)
          {
            C = sqrt(long double(j));
            if(C == (__int64)C)
              {
                a = to_string((__int64)C);
                ispal = true;
                int asize = a.size();
                for(int k = 0 ; k < asize / 2; ++k)
                  if(a[k] != a[asize - 1 - k])
                    {
                    ispal = false;
                    break;
                    }
                  if(ispal)
                    ++counter;
              }
          }

        }
    res[i] = counter;
    }

  for(int i = 0 ; i < T ; ++i)
    {
    g << "Case #" << i + 1 << ": ";
    g << res[i] << '\n';
    }

  return 0;
  }