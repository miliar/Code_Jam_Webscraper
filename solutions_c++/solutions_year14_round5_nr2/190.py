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

int p, q, n;
VI h, g;
VVI din;

int calc (int a, int acum)
{
  if (a >= n) return 0;
  if (din[a][acum] > -1) return din[a][acum];
  int nec = (h[a]+q-1)/q;
  int ans = calc (a+1,acum + nec);
  int rest = h[a]-(nec-1)*q;
  int nec2 = (rest+p-1)/p;
  int ac2 = acum + nec-1;
  if (nec2 <= ac2)
    ans = max (ans, g[a] + calc(a+1,ac2-nec2));
//     cout << a << " " << ac2 << " " << ans << endl;
  return din[a][acum] = ans;
}

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso ++)
  {
    cout << "Case #" << caso << ": ";
    cin >> p >> q >> n;
    h = g = VI (n);
    fi (n) cin >> h[i] >> g[i];
    din = VVI (n, VI (12*(n+7),-1));
    cout << calc (0,1) << endl;
  }
}