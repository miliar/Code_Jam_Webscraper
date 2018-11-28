#include <iostream>
#include <vector>

using namespace std;

uint64_t pw(uint64_t b, uint64_t e)
{
  uint64_t r = 1;
  while (e)
  {
      if (e & 1)
        r *= b;
      e >>= 1;
      b *= b;
  }
  return r;
}
int main(void)
{
  uint64_t TN;
  cin >> TN;
  for (uint64_t CN = 1; CN <= TN; ++CN)
  {
    cout << "Case #" << CN << ": ";
    uint64_t K, C, S;
    cin >> K >> C >> S; // 1 1 1
    if (C == 1)
    {
      if (K > S)
        cout << "IMPOSSIBLE";
      else
      {
        for (uint64_t i = 1; i <= K; ++i)
        {
          cout << i << " ";
        }
      }
    }
    else if ((K+1)/2 > S)
      cout << "IMPOSSIBLE";
    else
    {
      uint64_t W = pw(K, C-1);
      for (uint64_t i = 0; i < K/2; i++)
      {
        cout << (2*i * W + 2*i + 1 + 1) << " ";
      }
      if (K%2 == 1)
      {
        cout << ((K - 1) * W + K) << " ";
      }
    }
    cout << endl;
  }
}
