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
  int L, X;
  scanf("%d%d", &L, &X);
  
  char mot[L+1];
  scanf("%s", mot);
  
  int quat[4][4] = {{0, 1, 2, 3},
                    {1, 0, 3, 2},
                    {2, 3, 0, 1},
                    {3, 2, 1, 0}};
  int sign[4][4] = {{1, 1, 1, 1},
                    {1, -1, 1, -1},
                    {1, -1, -1, 1},
                    {1, 1, -1, -1}};
  
  int act = 0;
  
  int sig = 1;
  int val = 0;
  for (int i=0; i<X*L; i++)
  {
    sig *= sign[val][mot[i%L]-'i'+1];
    val = quat[val][mot[i%L]-'i'+1];
    if (act == 0 && val == 1 && sig == 1) act++;
    else if (act == 1 && val == 3 && sig == 1) act++;
  }
  
  if (act == 2 && val == 0 && sig == -1)
    printf("YES\n");
  else
    printf("NO\n");
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
