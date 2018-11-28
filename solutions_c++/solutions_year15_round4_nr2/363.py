#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 1e-14
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
typedef vector<string> VS;
typedef map<char,int> MCI;
typedef vector<PD> VPD;

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout.setf(ios::fixed);
    cout.precision(10);
    cout << "Case #" << caso << ": ";
    int n;
    double v, x;
    cin >> n >> v >> x;
    VPD tf (n);
    fi (n) cin >> tf[i].second >> tf[i].first;
    sort(tf.begin(),tf.end());
    
    double mn = 0;
    double mx = 1e30;
    while (min((mx - mn)/mn, mx-mn) > eps)
    {
      double md = (mx + mn) / 2.;
//       cout << mn << " " << md << " " << mx << endl;
      VD vol (n);
      double sv = 0;
      fi (n) sv += vol[i] = md * tf[i].second;
      if (sv < v)
      {
        mn = md;
        continue;
      }
      double vt = 0;
      double tp = 0;
      int ii = 0;
      while (vt < v - eps)
      {
        double qd = min(v-vt, vol[ii]);
        tp = (tp*vt + qd * tf[ii].first) / (vt + qd);
        vt += qd;
        ii++;
      }
      if (tp > x + eps)
      {
        mn = md;
        continue;
      }
      
      vt = 0;
      tp = 0;
      ii = n-1;
      while (vt < v - eps)
      {
        double qd = min(v-vt, vol[ii]);
        tp = (tp*vt + qd * tf[ii].first) / (vt + qd);
        vt += qd;
        ii--;
      }
//       cout << tp << " " << x << endl;
      if (tp < x - eps)
      {
        mn = md;
        continue;
      }
      
      
//       cout << "ok" << endl;
      
      mx = md;
    }
    double ans = (mx + mn) / 2.;
    if (ans > 1e29) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
    
  }
}