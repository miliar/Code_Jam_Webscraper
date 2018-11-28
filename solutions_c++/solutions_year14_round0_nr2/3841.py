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
    double c, f, x;
    cin>>c>>f>>x;
    double czas=0, pr=2, wyn=x/pr;
    while (czas<wyn)
    {
      wyn=min(wyn, czas+x/pr);
      czas+=c/pr;
      pr+=f;
    }
    cout.precision(7);
    cout<<"Case #"<<ca<<": "<<fixed<<wyn<<endl;
  }

  return 0;
}
