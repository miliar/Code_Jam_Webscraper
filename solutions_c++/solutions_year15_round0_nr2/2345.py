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
  for (int ca=1; ca<=NNN; ++ca)
  {
    int d, ile[1001]={}, ma=0;
    cin>>d;
    Fori(d)
    {
      int a;
      cin>>a;
      ma=max(ma, a);
      ++ile[a];
    }
    int wyn=ma;
    for (int czasJedz=1; czasJedz<wyn; ++czasJedz)
    {
      int lPrzekl=0;
      for (int i=czasJedz+1; i<=ma; ++i)
        lPrzekl+=((i+czasJedz-1)/czasJedz-1)*ile[i];
      wyn=min(wyn, czasJedz+lPrzekl);
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
