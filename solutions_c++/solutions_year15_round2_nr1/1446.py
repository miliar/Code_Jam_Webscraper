#include <bits/stdc++.h>
#define MAX 1111111
typedef long long int lli;
using namespace std;
 
lli xx[MAX];
 
lli xyz(int x)
{
  lli abc = 0;
  while (x > 0)
  {
    abc = abc * 10 + (x % 10);
    x /= 10;
  }
  return abc;
}
 

int main()
{
  queue<lli> ns;
  lli a,b,c;
  memset(xx,0,sizeof(xx));
  xx[1] = 1;
  ns.push(1);
  while (!ns.empty())
  {
    lli x = ns.front();
    ns.pop();
    if (x + 1 < MAX and xx[x + 1] == 0)
    {
      xx[x + 1] = xx[x] + 1;
      ns.push(x + 1);
    }
    if (xyz(x) < MAX and xx[xyz(x)] == 0)
    {
      xx[xyz(x)] = xx[x] + 1;
      ns.push(xyz(x));
    }
  }

  lli testcase;
  cin >> testcase;
  for (lli t = 1; t <= testcase; t++)
  {
    lli n;
    cin >> n;
    printf("Case #%lld: %lld\n", t, xx[n]);
  }
  return 0;
}
