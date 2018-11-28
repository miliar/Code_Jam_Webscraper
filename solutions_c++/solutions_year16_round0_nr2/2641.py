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
    string s;
    cin>>s;
    int wyn=0;
    for (int i=0; i<s.size(); ++i)
    {
      if (s[i]=='-')
      {
        if (0<i && s[i-1]=='-')
          continue;
        if (0<i)
          ++wyn;
        ++wyn;
      }
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
