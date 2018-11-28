#include <stdio.h>
#include<iostream>
#include<cstdlib>
#include<climits>

using namespace std;

long CHECK = -1;

void solve(long N)
{
  long X = N;
  if (N == 0)
    {
      cout << "INSOMNIA" << endl;
      return;
    }
  if (CHECK == -1)
    {
      CHECK = 0;
      for (int i = 0; i < 10; i++)
        {
          CHECK |= (1<<i);
        }
    }
  int i = 1, k = 0;
  long ND = X;
  do {
      ND = X;
      while (ND)
        {
          k = (k | (1 << ((ND%10))));
          ND /= 10;
        }
      if (k == CHECK)
        {
          cout << X << endl;
          return;
        }

      i++;
      X = N*i;
  } while(1);
}

int main()
{
  int T = 0;
  cin >> T;

  for (int i = 0; i < T; i++)
    {
      long N;
      cin >> N;
      cout << "Case #" << i+1 << ": ";
      solve(N);
    }
  return 0;
}
