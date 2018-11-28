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

void szukaj(int n, int j)
{
  for (int a=0; a<n; ++a)
    for (int b=0; b<n; ++b)
      for (int d=0; a+b+d+10<=n; ++d)
      {
        cout<<11;
        for (int c=0; c<a; ++c)
          cout<<0;
        cout<<11;
        for (int c=0; c<b; ++c)
          cout<<0;
        cout<<11;
        for (int c=0; c<d; ++c)
          cout<<0;
        cout<<11;
        for (int c=0; a+b+c+d+10<n; ++c)
           cout<<0;
        cout<<11;
           
        for (int c=3; c<=11; ++c)
          cout<<' '<<c;
        cout<<endl;
        if (--j==0)
          return;
      }
  cout<<"xxxxx"<<endl;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    int n, j;
    cin>>n>>j;
    cout<<"Case #"<<ca<<": "<<endl;
    szukaj(n, j);
  }

  return 0;
}
