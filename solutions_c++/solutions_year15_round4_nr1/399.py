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
typedef vector<string> VS;
typedef map<char,int> MCI;

int di[4] = {0,1,0,-1};
int dj[4] = {1,0,-1,0};

VS mapa;
int R, C;

string dac = ">v<^";
MCI cad;

bool sale (int i, int j, int d)
{
  if (i < 0 or i >= R or j < 0 or j >= C) return true;
  if (mapa[i][j] != '.') return false;
  return sale (i+di[d], j+dj[d], d);
}

int main()
{
  fi(4) cad[dac[i]] = i;
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    cin >> R >> C;
    mapa = VS (R);
    fi(R) cin >> mapa[i];
    int ans = 0;
    bool pos = true;
    fi(R) fj(C)
    {
      if (mapa[i][j] == '.') continue;
      VB val(4);
      fk (4) val[k] = sale(i+di[k],j+dj[k],k);
      int dc = cad[mapa[i][j]];
      if (val[dc])
      {
        bool ps = false;
        fk(4) if (not val[k])
        {
          ans++;
          ps = true;
          break;
        }
        if (not ps) pos = false;
      }
    }
    if (not pos) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
}