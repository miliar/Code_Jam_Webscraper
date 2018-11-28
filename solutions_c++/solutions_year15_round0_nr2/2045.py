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

int N;
int tab[1000];

void main2()
{
  scanf("%d", &N);
  for (int i=0; i<N; i++)
    scanf("%d", &tab[i]);
  
  int best = 1000000000;
  for (int maxi=1; maxi<=1000; maxi++)
  {
    int res = maxi;
    for (int i=0; i<N; i++)
      res += tab[i]/maxi + (tab[i] % maxi > 0) - 1;
    best = min(best, res);
  }
  
  printf("%d\n", best);
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
