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
    int sm, ile=0, bylo=0;
    string s;
    cin>>sm>>s;
    Fori(sm+1)
    {
      int a=s[i]-'0';
      if (!a)
        continue;
      if (bylo<i)
      {
        int b=i-bylo;
        bylo+=b;
        ile+=b;
      }
      bylo+=a;
    }
    cout<<"Case #"<<ca<<": "<<ile<<endl;
  }
  return 0;
}
