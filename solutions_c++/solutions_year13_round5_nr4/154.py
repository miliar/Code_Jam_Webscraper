#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>

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
typedef map<ll,ll> MLL;
typedef map<int,double> MSD;

MSD din;
int n;

int transf (string s)
{
  int ans = 0;
  fi (n)
  {
    ans *= 2;
    ans += (s[n-i-1] == '.'?1:0);
  }
  return ans;
}

double calc (int s)
{
  if (din.find(s) != din.end())
    return din[s];
  if (s == 0) return 0;
  double ans = 0;
  fi (n)
  {
    int ii = i;
    int mon = n;
    while (not (s&(1<<ii)))
    {
      ii++;
      ii %= n;
      mon --;
    }
    ans += mon + calc(s - (1<<ii));
  }
  return din[s] = ans / n;
  
}

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    string s;
    cin >> s;
    n = s.size();
    din = MSD();
    cout.setf(ios::fixed);
    cout.precision(12);
    cout << "Case #" << caso << ": " << calc (transf(s)) << endl;
  }
}