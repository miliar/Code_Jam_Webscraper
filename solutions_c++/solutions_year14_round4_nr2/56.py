#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;

int main()
{
  int t;
  cin >> t;
  for (int caso = 1; caso <= t; caso++)
  {
    cout << "Case #" << caso << ": ";
    int n;
    cin >> n;
    VI v(n);
    fi (n) cin >> v[i];
    int sm = 0;
    int m = n;
    fi (n)
    {
      int pm = 0;
      fj (m) if (v[pm] > v[j]) pm = j;
      sm += min (pm, m-pm-1);
      VI w (m-1);
      fj (pm) w[j] = v[j];
      fjj (pm+1,m) w[j-1] = v[j];
      m--;
      v = w;
    }
    cout << sm << endl;
  }
}