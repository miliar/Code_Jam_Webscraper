#include <stdio.h>
#include <algorithm>
#include <set>
#include <cmath>

#define MAX 101
using namespace std;

int main() {
  //freopen("input.inp", "rt", stdin);
  //freopen("output.oup", "wt", stdout);   
  
  int t, n;
  set<int> digits;
  long long val, tmp;
  int c = 0;
  
  scanf("%d", &t);
  while (t--)
  {
    ++c;
    printf("Case #%d: ", c);
    digits.clear();
    scanf("%d", &n);
    if (n == 0)
    {
      printf("INSOMNIA\n");
      continue;
    }
    val = 0;
    while (digits.size() < 10)
    { 
      val += n;
      tmp = val;
      while (tmp)
      {
        digits.insert(tmp % 10);
        tmp /= 10;
      }      
    }
    printf("%I64d\n", val);
  }
  
  return 0;
}