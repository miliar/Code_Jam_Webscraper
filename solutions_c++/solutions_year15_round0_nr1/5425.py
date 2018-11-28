#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

#define x first 
#define y second
#define mp make_pair
#define pb push_back
#define sz(v) (int)(v).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)

typedef long long ll;
typedef long double ld;

const int inf = (int)(2e9);                                                                       
const ld eps = 1e-12;

#define file "a"
const int N = 100500;

char s[N];
int n;
                   
int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int test;
  scanf("%d", &test);
  for (int t = 0; t < test; t++)
  {
    scanf("%d ", &n);
    scanf("%s", s);
    assert(n + 1 == (int)strlen(s));
    int sum = 0, ans = 0;
    for (int i = 0; i < n + 1; i++)
    {
      if (s[i] == '0')
      	continue;
      
      if (sum >= i)
      	sum += s[i] - '0';
      else
      {
        ans += i - sum;
        sum = i;
        sum += s[i] - '0';
      }
    }
    printf("Case #%d: %d\n", t + 1, ans);
  }

  return 0;
}