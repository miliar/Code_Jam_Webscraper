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


    int n;
    bool u[4][4]={};//[p][m]

bool umie(int p, int m, int d)
{
  return u[p][m] || (d&(1<<(p*n+m)));
}

bool ok(int d, bool zp[], bool zm[])
{
  for (int p=0; p<n; ++p)
    if (!zp[p])
    {
      zp[p]=true;
      bool bm=false;
      for (int m=0; m<n; ++m)
        if (!zm[m] && umie(p, m, d))
        {
          bm=true;
          zm[m]=true;
          if (!ok(d, zp, zm))
            return false;
          zm[m]=false;
        }
      if (!bm)
       return false;
      zp[p]=false;
      
    }

  return true;
}

bool ok(int d)
{
  bool zp[4]={}, zm[4]={};
  return ok(d, zp, zm);
}


int lb(int a)
{
  int wyn=0; 
  while (a)
  {
    if (a&1)
      ++wyn;
    a/=2;
  }
  return wyn;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    cin>>n;
    memset(u, 0, sizeof(u));
    for (int i=0; i<n; ++i)
    {
      string s;
      cin>>s;
      for (int j=0; j<n; ++j)
        if (s[j]=='1')
          u[i][j]=true;
    }
    int wyn=100;
    for (int x=(1<<(n*n))-1; x>=0; --x)
    {
      int l=lb(x);
      if (l>=wyn)
        continue;
      if (ok(x))
        wyn=l;
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
