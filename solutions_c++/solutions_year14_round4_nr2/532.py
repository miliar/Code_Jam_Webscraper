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
    int n, wyn=0;
    cin>>n;
    VI a(n);
    Fori(n)
      cin>>a[i];
    while (a.size())
    {
      int ind=0;
      Fori(a.size())
        if (a[i]<a[ind])
          ind=i;
      wyn+=min((unsigned) ind, a.size()-1-ind);
      a.erase(a.begin()+ind);
    }  
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
