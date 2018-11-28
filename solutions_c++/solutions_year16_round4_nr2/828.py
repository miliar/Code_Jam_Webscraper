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


double licz(double x[], int k)
{
    vector<double> dt(k+1, 0);
    dt[0]=1;
    Fori(k)
    {
      double dk=x[i];
      vector<double> a(k+1, 0);
      for (int j=1; j<k+1; ++j)
        a[j]=dt[j-1]*dk;
      dk=1-dk;
      for (int j=0; j<k+1; ++j)
        a[j]+=dt[j]*dk;
    
      dt.swap(a);
    }
    return dt[k/2];
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
    int n, k;
    cin>>n>>k;
    double p[200], x[200];
    Fori(n)
      cin>>p[i];
    sort(p, p+n);
    int kk=0;
    Fori(k)
    {
      x[kk++]=p[i];
      x[kk++]=p[n-1-i];
    }
    double wyn=0;
    for (int a=(1<<n)-1; a>0; --a)
    {
      if (lb(a)!=k)
        continue;
      int po=0;
      for (int i=0; i<n; ++i)
        if (a&(1<<i))
          x[po++]=p[i];
      wyn=max(wyn, licz(x, k));
    }
    
  
  
  
  
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
