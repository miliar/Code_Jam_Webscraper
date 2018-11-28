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

const int P=0, R=1, S=2;

string liczP(int n);
string liczR(int n);
string liczS(int n);

string liczP(int n)
{
  if (n==0)
    return "P";
  string a=liczP(n-1), b=liczR(n-1);
  return a<b ? a+b : b+a;
}

string liczR(int n)
{
  if (n==0)
    return "R";
  string a=liczR(n-1), b=liczS(n-1);
  return a<b ? a+b : b+a;
}

string liczS(int n)
{
  if (n==0)
    return "S";
  string a=liczS(n-1), b=liczP(n-1);
  return a<b ? a+b : b+a;
}

int n, r, p, s;

bool dobry(string z)
{
  int pp=0, rr=0, ss=0;
  for (int i=0; i<z.length(); ++i)
    switch (z[i])
    {
      case 'P': ++pp; break;
      case 'R': ++rr; break;
      case 'S': ++ss; break;
    }
  return p==pp && r==rr && s==ss;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    cin>>n>>r>>p>>s;
    string t[]={liczP(n), liczR(n), liczS(n)};
    sort(t, t+3);
    string wyn;
    if (dobry(t[0])) wyn=t[0];
    else if (dobry(t[1])) wyn=t[1];
    else if (dobry(t[2])) wyn=t[2];
    else wyn="IMPOSSIBLE";
  
  
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
