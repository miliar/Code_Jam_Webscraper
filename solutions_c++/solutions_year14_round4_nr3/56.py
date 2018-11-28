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
typedef pair<ll,int> PLI;
typedef priority_queue<PLI> PQPLI;

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    ll w, h;
    int b;
    cin >> w >> h >> b;
    VL x0,x1,y0,y1;
    x0 = x1 = y0 = y1 = VL (b);
//     cout << "ok" << b << endl;
    fi (b)
    {
      cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
    }
    x0.push_back(-1);
    x1.push_back(-1);
    y0.push_back(0);
    y1.push_back(h-1);
    x0.push_back(w);
    x1.push_back(w);
    y0.push_back(0);
    y1.push_back(h-1);
    b+=2;
    VVL g (b, VL (b));
    fi (b) fj(b)
    {
      ll dx = max (0LL,max(x0[i]-x1[j]-1,x0[j]-x1[i]-1));
      ll dy = max (0LL,max(y0[i]-y1[j]-1,y0[j]-y1[i]-1));
      g[i][j] = max(dx,dy);
//       cout << i << " " << j << " " << g[i][j] << endl;
    }
    
    VB vis (b, false);
    VL dis (b, 1LL<<60);
    PQPLI q;
    q.push(PLI(0,b-2));
    dis[b-2] = 0;
    while (not vis[b-1])
    {
      int a = q.top().second;
      q.pop();
      if (vis[a]) continue;
      vis[a] = true;
      fi (b)
      {
        ll nd = dis[a] + g[a][i];
        if (nd < dis[i])
        {
          dis[i] = nd;
          q.push(PLI(-nd,i));
        }
      }
    }
    cout << dis[b-1] << endl;
  }
}