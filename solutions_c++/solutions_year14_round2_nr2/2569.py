// question #:
// author: SUN, Ka Meng Isaac (skmisaac)
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <vector>
#include <stack> 
#include <queue> 
#include <deque> 
#include <bitset> 
#include <algorithm> 
#include <set> 
#include <list> 

using namespace std;

typedef long long       ll;
typedef pair<int, int>  ii;
typedef vector<ii>      vii;
typedef vector<int>     vi;
#define INF             1000000000
#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

#define modulo(S, N) ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))

int main(int argc, char const *argv[])
{
  int tc;
  scanf("%d", &tc);

  for (int i = 1; i <= tc; ++i)
  {
    int won = 0;
    int A, B, K;
    scanf("%d %d %d", &A, &B, &K);

    for (int j = 0; j < A; ++j)
    {
      for (int k = 0; k < B; ++k)
      {
        if ( (j & k) < K )
        {
          won++;
        }
      }
    }


    
    printf("Case #%d: %d\n", i, won);
  }


  return 0;
}
