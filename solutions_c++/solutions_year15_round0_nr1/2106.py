#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

#define INF                         1000000000
#define EPS                         1e-9
#define INDEF                       -1

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define fill(a,v)                   memset(a, v, sizeof a)
#define size(a)                     ((int)(a.size()))

#define ll long long int

// ------------------------------------------------------- //

void main2()
{
  int N;
  scanf("%d ", &N);
  int act = 0;
  int res = 0;
  for (int i=0; i<=N; i++)
  {
    if (act < i)
    {
      res += i - act;
      act += i - act;
    }
    act += getchar() - '0';
  }
  
  printf("%d\n", res);
}

int main()
{
  int N;
  scanf("%d", &N);
  for (int i=1; i<=N; i++)
  {
    printf("Case #%d: ", i);
    main2();
  }
}
