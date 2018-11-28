#include <cstdio>
#include <cmath>

using namespace std;

#define MAX_N 10000000
#define MAX_L 7

int a,b,l,g;
int n;

int pal[MAX_N];
int start[MAX_L+2];
int good[MAX_N];

void palindrome(int len)
{
  int n;
  pal[0] = 0;
  for (n=0; n<=9; n++)
    pal[n+1] = n;
  n++;
  start[0] = 0;
  start[1] = 1;
  for (int l=2; l<=len; l++)
  {
    start[l] = n;
    for (int j=1; j<=9; j++)
    {
      for (int k=l%2; k<=l-2; k+=2)
      {
        for (int i=start[k]; i<start[k+1]; i++)
        {
          int t2 = pal[i] * pow(10,(l-2-k)/2);
          t2 += j * pow(10,l-2);
          t2 *= 10;
          pal[n] = t2 + j;
          n++;
        }
      }
    }
  }
  start[len+1] = n;
}

bool check_pal(int n)
{
  int rev = 0;
  int orig = n;
  while (n>0)
  {
    rev = rev * 10 + n %10;
    n /= 10;
  }
  return orig == rev;
}

void find_good(int len)
{
  g=0;
  for (int i=start[1]+1; i<start[len+1]; i++)
  {
    int t = pow(pal[i],2);
    if (check_pal(t))
    {
      good[g] = t;
      g++;
    }
  }
}

int main()
{
  int t;
  palindrome(7);
  find_good(7);
  //for (int i=0; i<g; i++)
  //  printf("%d\n",good[i]);
  scanf("%d",&t);
  for (int k=0; k<t; k++)
  {
    scanf("%d %d",&a,&b);
    int count = 0;
    for (int i=0; i<g; i++)
    {
      if (good[i]>=a && good[i]<=b)
      {
          count++;
      }
    }
    printf("Case #%d: %d\n",k+1, count);
  }
  return 0;
}
