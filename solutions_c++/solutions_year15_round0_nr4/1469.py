#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

int main()
{
  int NNN;
  cin>>NNN;
  string ulozy="GABRIEL\n", nieUlozy="RICHARD\n";
  for (int ca=1; ca<=NNN; ++ca)
  {
    int x, r, c;
    cin>>x>>r>>c;
    if (c<r)
      swap(c, r);
    cout<<"Case #"<<ca<<": ";
    if (r*c%x || 7<=x)
    {
      cout<<nieUlozy;
      continue;
    }
    if (c<x || r<(x+1)/2)
    {
      cout<<nieUlozy;
      continue;
    }
    if ((x+1)/2<r)
    {
      cout<<ulozy;
      continue;
    }
    bool u=true;
    for (int zL=1; zL<(x+1)/2 && u; ++zL)
    {
      u=false;
      for (int wk=0; wk<=c-(x+1)/2; ++wk)
        if ((wk*r+zL*(r-1))%x==0)
        {
          u=true;
          break;
        }
    }
    
    cout<<(u ? ulozy : nieUlozy);
  }
  return 0;
}
