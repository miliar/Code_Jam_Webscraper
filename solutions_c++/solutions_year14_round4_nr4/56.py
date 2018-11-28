#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
#include <set>

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
typedef pair<ll,int> PLI;
typedef priority_queue<PLI> PQPLI;
typedef set<string> SS;
typedef vector<SS> VSS;
typedef vector<string> VS;


int m, n;
VI dist;
VS pal;
int mx, tot;

void back (int a)
{
  if (a == m)
  {
    VSS v(n);
    fi (m)
    {
//       cout << "antes" << endl;
      fj (pal[i].size()+1)
      {
//         cout << pal[i].size() << " " << j << endl;
        v[dist[i]].insert(pal[i].substr(0,j));
      }
//       cout << "despues" << endl;
    }
    ll ans = 0;
    fi (n) if (v[i].size() == 0) return;
    fi (n) ans += v[i].size();
    if (ans > mx)
    {
      mx = ans;
      tot = 1;
    }
    else if (ans == mx) tot++;
    return;
  }
  fi (n)
  {
    dist[a] = i;
    back (a+1);
  }
}

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    cin >> m >> n;
    pal = VS (m);
    fi (m) cin >> pal[i];
    dist = VI (m);
    mx = tot = 0;
    back (0);
    cout << mx << " " << tot << endl;
  }
}