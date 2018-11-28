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

  int T,Smax,a[2000],j,no,sol,k,s;
  string line;
  cin>>T;
  for(int i=0;i<T;i++)
  {
      printf("Case #%d:",i+1);
      cin>>Smax;
      cin>>line;
      k=Smax;
      int y=0;
      for(int x=0;x<line.length()-1;++x)
        {
     a[y]=(int)line[x]-48;
     y++;}
      k=0;
      sol=0;
      s=0;
      int m=0;
      if(a[0]==0)
        m=1;
        while(k<=Smax)
        {
            m=0;
            if((k>s))
                m=k-s;
            sol=sol+m;
            s=s+a[k]+m;
            k++;

        }
      printf(" %d\n",sol);
  }
  return 0;
}
