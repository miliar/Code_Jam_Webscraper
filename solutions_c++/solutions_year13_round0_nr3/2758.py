#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <inttypes.h>
using namespace std;

bool isPal(unsigned long long k, bool p)
{
  int len = 0;
  int digits[101] = {0};
  while(k>0)
  {
    digits[len++] = k%10;
    k /= 10;
  }

  for(int i = 0; i < len/2; ++i)
    if(digits[i] != digits[len-1-i]) return false;


  if (false && p)
  {
    for (int i = len-1; i >= 0; --i)
      cout<<digits[i];
    cout<<endl;
  }


  return true;
}

int main()
{
  freopen("C-small-attempt0.in", "rt", stdin);
  freopen("C-small-attempt0.out", "wt", stdout);

  int T;
  int A, B;

  cin>>T;
  
  for (int t=1; t<=T; t++)
  {
    printf("Case #%d: ", t);

    cin>>A>>B;
    unsigned long long a = ceil(sqrt(A));
    unsigned long long b = sqrt(B);
    int count = 0;
    for (unsigned long long k = a; k <= b; ++k)
    {
      if (isPal(k, false) && isPal(k*k, true)) ++count;
    } 

    printf("%d\n", count);
  }
}
