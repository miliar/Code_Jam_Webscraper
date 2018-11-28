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
    int w1, w2, t1[4][4], t2[4][4];//[w][k]
    cin>>w1;
    --w1;
    for (int i=0; i<4; ++i)
      for (int j=0; j<4; ++j)
        cin>>t1[i][j];
    cin>>w2;
    --w2;
    for (int i=0; i<4; ++i)
      for (int j=0; j<4; ++j)
        cin>>t2[i][j];
    int ile=0, wyn=0;
    for (int i=0; i<4; ++i)
      for (int j=0; j<4; ++j)
        if (t1[w1][i]==t2[w2][j])
        {  
          ++ile;
          wyn=t1[w1][i];
        }
    cout<<"Case #"<<ca<<": ";
    if (ile==0) cout<<"Volunteer cheated!\n";
    else if (ile==1) cout<<wyn<<endl;
    else cout<<"Bad magician!\n";
  }

  return 0;
}
