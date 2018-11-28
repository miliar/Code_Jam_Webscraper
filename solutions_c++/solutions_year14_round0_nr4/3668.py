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
    int n;
    cin>>n;
    double t1[1000], t2[1000];
    for (int i=0; i<n; ++i)
      cin>>t1[i];
    for (int i=0; i<n; ++i)
      cin>>t2[i];
    sort(t1, t1+n);
    sort(t2, t2+n);
    
/*    for (int i=0; i<n; ++i)
      cout<<t1[i]<<' ';
    cout<<endl;
    for (int i=0; i<n; ++i)
      cout<<t2[i]<<' ';
    cout<<endl;*/
    
    int oryg=0, osz=0;
    for (int poz1=0, poz2=0; poz1<n && poz2<n; )
    {
      if (t1[poz1]<t2[poz2])
      {
        ++poz1;
        continue;
      }
      ++osz;
      ++poz1;
      ++poz2;
    }
  
    for (int poz1=0, poz2=0; poz1<n; )
    {
      if (poz2>=n)
      {
        ++oryg;
        ++poz1;
        continue;
      }
      if (t1[poz1]<t2[poz2])
      {
        ++poz1;
        ++poz2;
        continue;
      }
      ++poz2;
    }
  
    
    cout<<"Case #"<<ca<<": "<<osz<<' '<<oryg<<endl;
  }


  return 0;
}
