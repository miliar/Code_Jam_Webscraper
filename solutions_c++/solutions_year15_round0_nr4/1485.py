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

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  int x, r, c, flag;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++)
  {
      printf("Case #%d: ", qq);

      cin>>x>>r>>c;
      if (x>=7)
      {
          flag=0;
      }
      else if (x==1)
      {
          flag=1;
      }
      else if (((r*c)%x)!=0)
      {
          flag=0;
      }
      else if (x==2)
      {
          flag=1;
      }
      else if (x==3)
      {
          if (((r>=3) && (c>=2))||((r>=2) && (c>=3)))
            flag=1;
          else
            flag=0;
      }
      else if (x==4)
      {
          if (((r>=3) && (c>=4))||((r>=4) && (c>=3)))
            flag=1;
          else
            flag=0;
      }
      else if (x==5)
      {
          if (((r>=5) && (c>=4))||((r>=4) && (c>=5)))
            flag=1;
          else
            flag=0;
      }
      else if (x==6)
      {
          if (((r>=6) && (c>=4))||((r>=4) && (c>=6)))
            flag=1;
          else
            flag=0;
      }

      if (flag==0)
        cout<<"RICHARD\n";
      else
        cout<<"GABRIEL\n";

  }

  return 0;
}
