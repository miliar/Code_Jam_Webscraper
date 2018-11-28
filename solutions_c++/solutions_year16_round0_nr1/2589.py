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


long long znajdz(int n)
{
  bool byly[10]={};
  int lc=0;
  for (long long i=1; ; ++i)
  {
    long long a=n*i;
    while (a)
    {
      int c=a%10;
      a/=10;
      if (!byly[c])
      {
        byly[c]=true;
        ++lc;
      }
    }
    if (lc==10)
      return n*i; 
  }
}

int main()
{
 /* long long a=0;
  for (int i=1; i<1000000; ++i)
  {
    a=max(a, znajdz(i));
    if (i%10000==0)
      cout<<i<<endl;
  }
  cout<<a<<endl;*/

  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    int n;
    cin>>n;
    cout<<"Case #"<<ca<<": ";
    if (n==0)
    {
      cout<<"INSOMNIA"<<endl;
      continue;
    }
    cout<<znajdz(n)<<endl;
    
  }

  return 0;
}
