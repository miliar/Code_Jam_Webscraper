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


int n, m, gdzie[1000], najW, najS;
VS s;

int ileW(int g)
{
  set<string> q;
  Fori(m)
    if (gdzie[i]==g)
    {
      string x=s[i];
      for (int j=0; j<=x.size(); ++j)
        q.insert(x.substr(0, j));      
    }
  return q.size();
}

void licz(int ktory)
{
  if (ktory<m)
  {
    for (gdzie[ktory]=0; gdzie[ktory]<n; ++gdzie[ktory])
      licz(ktory+1);
    return;
  }
  int lw=0;
  for (int i=0; i<n; ++i)
  {
    int x=ileW(i);
    if (x==0)
      return;
    lw+=x;
  }
  if (lw>najW)
  {
    najW=lw;
    najS=1;
  }
  else if (lw==najW)
    ++najS;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    najW=najS=0;
    s.clear();
    cin>>m>>n;
    Fori(m)
    {
      string a;
      cin>>a;
      s.push_back(a);
    }
    licz(0);  
    cout<<"Case #"<<ca<<": "<<najW<<' '<<najS<<endl;
  }


  return 0;
}
