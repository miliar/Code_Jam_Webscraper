#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = int(1e9) + 2;



int main()
{
#ifdef MY_DEBUG
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif


  int t = 0;
  cin >> t;
  char answer[32];
  const int dig = 10;
  vector<int> tmp(dig);
  for(int i = 1; i <= t; i++)
  {
    long long int n = 0;
    cin >> n;

    if(n==0)
    {
      sprintf(answer, "Case #%d: INSOMNIA", i);
      cout << answer << endl;
      continue;
    }
    tmp.assign(dig, 0);
    long long j = 1;
    int r = 0;
    long long int a = 0;
    while(r < dig)
    {
      a = j*n;
      long long b = a;
      j++;
      while(b && (r < dig))
      {
        int rad = b %10;
        b/=10;
        if(!tmp[rad])
        {
          tmp[rad] = 1;
          r++;
        }
      }
    }
    sprintf(answer, "Case #%d: %lld", i, a);
    cout << answer << endl;
  }
 
  return 0;
}
