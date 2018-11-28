#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

vector <int> b;

int main() {
  freopen("larin", "r", stdin);
  freopen("larout", "w", stdout);
  int tt;

  int d, i, p, s, res, tot;

  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++)
  {
      printf("Case #%d: ", qq);
      cin>>d;
      for (i=0; i<d; i++)
      {
          cin>>p;

          b.push_back(p);
      }
      sort(b.begin(), b.end());
      res=b.back();
      s=2;
      while (s<res)
      {
          tot=0;
          for (i=0; i<b.size(); i++)
          {
              tot+=(b[i]-1)/s;
          }
          tot+=s;
          if (tot<res)
          {
              res=tot;
          }
          ++s;
      }
      cout<<res<<endl;

      b.clear();



  }
  return 0;
}
