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
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    int n; cin >> n;
    ll p, q, r, s;
    cin >> p >> q >> r >> s;
    VL v(n);
    fi (n) v[i] = (i*p+q)%r+s;
    VL sm (n+1,0);
    fii (1,n+1) sm[i] = sm[i-1] + v[i-1];
    ll mn = 0;
    ll mx = sm[n];
    while (mn < mx)
    {
      ll md = (mn+mx)/2;
      ll i1 = *(upper_bound(sm.begin(),sm.end(),md)-1);
      ll i2 = sm[n]-*(lower_bound(sm.begin(),sm.end(),sm[n]-md));
//       cout << md << " " << i1 << " " << i2 << endl;
      if (sm[n]-i1-i2 > md)
        mn = md+1;
      else
        mx = md;
    }
    cout.setf(ios::fixed);
    cout.precision(10);
    cout << 1-double(mn)/sm[n] << endl;
  }
}