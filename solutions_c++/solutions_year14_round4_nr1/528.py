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
    int wyn=0, n, p[10000], x;
    cin>>n>>x;
    Fori(n)
      cin>>p[i];
    sort(p, p+n);
    reverse(p, p+n);
    for (int i=0; i<n; ++i)
    {
      ++wyn;
      if (p[i]+p[n-1]<=x)
        --n;
    }
  
  
  
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
