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


int r, c, w;

map<long long, int> jaa;

bool strzal(long long sp, int k)
{
  return (sp&(1LL<<(20+k)))!=0;
}

bool pudlo(long long sp, int k)
{
  return (sp&(1LL<<k))!=0;
}

int lTraf(long long sp)
{
  int wyn=0;
  Fori(c)
    if (strzal(sp, i) && !pudlo(sp, i))
      ++wyn;
  return wyn;
}
int onTraf(long long sp, int k);
int onPud(long long sp, int k);

int ja(long long sp)
{
  int a=jaa[sp];
  if (a)
    return a;
  if (lTraf(sp)==w)
    return 0;
  int wyn=1000;
  Fori(c)
    if (!strzal(sp, i))
    {
      int x=onTraf(sp, i), y=onPud(sp, i);
     // cout<<sp<<' '<<x<<' '<<y<<endl;
      wyn=min(wyn, max(x, y));
    }
//  cout<<sp<<' '<<wyn<<endl;
  return jaa[sp]=wyn;
}

int onTraf(long long sp, int k)
{
  
  for (int i=0; i<=k-w; ++i)
    if (strzal(sp, i) && !pudlo(sp, i))
      return 0;
  for (int i=k+w; i<c; ++i)
    if (strzal(sp, i) && !pudlo(sp, i))
      return 0;
  int le=0, pr=0;
  for (int i=k-1; i>=0; --i)
    if (!strzal(sp, i) || !pudlo(sp, i)) ++le;
    else break;
  for (int i=k+1; i<c; ++i)
    if (!strzal(sp, i) || !pudlo(sp, i)) ++pr;
    else break;
  if (le+pr+1<w)
    return 0;
  return 1+ja(sp|(1LL<<(k+20)));
}

int onPud(long long sp, int k)
{
  
  int pt=-1, ot=-1;
  for (int i=0; i<c; ++i)
    if (strzal(sp, i) && !pudlo(sp, i))
    {
      pt=i;
      break;
    }
  for (int i=c-1; i>=0; --i)
    if (strzal(sp, i) && !pudlo(sp, i))
    {
      ot=i;
      break;
    }
  if (pt<k && k<ot)
    return 0;
  
  int nw=0;
  if (pt==-1)
  {
    int ten=0;
    for (int i=0; i<c; ++i)
      if (i!=k && !strzal(sp, i)) nw=max(nw, ++ten);
      else ten=0;
    if (nw<w)
      return 0;
  }
  else
  {
    int le=0, pr=0;
    for (int i=pt-1; i>=0; --i)
      if (i!=k && (!strzal(sp, i) || !pudlo(sp, i))) ++le;
      else break;
    for (int i=pt+1; i<c; ++i)
      if (i!=k && (!strzal(sp, i) || !pudlo(sp, i))) ++pr;
      else break;
    if (le+pr+1<w)
      return 0;
  }
  return 1+ja(sp|(1LL<<(k+20))|(1LL<<k));
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    cin>>r>>c>>w;
    jaa.clear();
    cout<<"Case #"<<ca<<": "<<((r-1)*((c+w-1)/w)+ja(0))<<endl;
  }

  return 0;
}
