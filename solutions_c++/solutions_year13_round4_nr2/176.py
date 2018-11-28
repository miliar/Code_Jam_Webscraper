#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <stack>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

#define mod 1000002013

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
typedef map<ll,ll> MLL;
typedef set<ll> SL;
typedef pair<ll,ll> PL;
typedef stack<PL> SPL;

ll calc (ll n, ll p, ll pn)
{
  ll ini = 0;
  ll fin = pn-1;
  while (ini < fin)
  {
    ll md = (ini+fin+1)/2;
    ll mj = md;
    ll pos = 0;
    ll sm = pn/2;
    fi (n)
    {
      if (mj == 0) break;
      pos += sm;
      sm /= 2;
      mj--;
      mj /= 2;
    }
//     cout << md << "->" << pos << endl;
    if (pos <= p-1)
      ini = md;
    else
      fin = md-1;
  }
  return ini;
}

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    ll n, p;
    cin >> n >> p;
    ll pn = 1;
    ll n2 = n;
    while (n2-- > 0) pn *= 2;
    if (p == pn) cout << pn-1 << " " << pn-1 << endl;
    else cout << calc (n,p,pn) << " " << pn-2-calc(n,pn-p,pn) << endl;
      
  }
}