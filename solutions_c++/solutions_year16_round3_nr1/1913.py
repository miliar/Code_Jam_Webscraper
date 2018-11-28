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
  for(int i = 0; i < t; i++)
  {
    cout << "Case #" << i+1 << ": ";
    int n =0;
    cin >> n;
    vector<int> p(n);
    int s = 0;
    for(int i = 0; i < n; i++)
    {
      cin >> p[i];
      s+=p[i];
    }

    int sz = int(p.size());
    while(s)
    {
      int ind = -1, e = -1;
      for(int i = 0; i < sz; i++)
      {
        if(p[i] > e)
        {
          ind = i;
          e = p[i];
        }
      }

      cout << char('A'+ind);
      p[ind]--;
      s--;

      if(s)
      {
        int last_ind = -1, e = -1;
        for(int i = 0; i < sz; i++)
        {
          if(p[i] > e)
          {
            last_ind = i;
            e = p[i];
          }
        }
        if((last_ind>=0)&&(2*p[last_ind] > s))
        {
          cout << char('A' + last_ind);
          p[last_ind]--;
          s--;
        }
      }
      cout << " ";
    }
    cout << endl;

  }


  return 0;
}
