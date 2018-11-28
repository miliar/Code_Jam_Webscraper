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

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    ll n, m;
    cin >> n >> m;
    MLL sub, baj;
    ll tot = 0;
    SL ind;
    fi (m)
    {
      ll a, b, c;
      cin >> a >> b >> c;
      sub[a] += c;
      sub[a] %= mod;
      baj[b] += c;
      baj[b] %= mod;
      ll d = (b-a)%mod;
      d = (d*(d-1))/2;
      d %= mod;
      d *= c;
      tot += d%mod;
      tot %= mod;
      ind.insert(a);
      ind.insert(b);
    }
    VL v(ind.begin(),ind.end());
    SPL cant;
    ll desc = 0;
    fi (ind.size())
    {
      int p = v[i];
      if (sub[p] > 0)
      {
        cant.push (PL (p, sub[p]));
      }
      while (baj[p] > 0)
      {
        ll ct = min (baj[p], cant.top().second);
        ll d = (p-cant.top().first)%mod;
        d = (d*(d-1))/2;
        d %= mod;
        d *= ct;
        desc += d%mod;
        desc %= mod;
        
        baj[p] -= ct;
        cant.top().second -= ct;
        if (cant.top().second == 0)
          cant.pop();
      }
    }
    cout << (desc - tot + mod) % mod << endl;
  }
}