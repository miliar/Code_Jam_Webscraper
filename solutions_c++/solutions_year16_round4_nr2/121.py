#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define x first
#define y second

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef pair < int, int > pii;

class magija{
public:
  double all[425];
  magija(){memset(all, 0, sizeof all);}
  double& operator[](int x){return all[x+212];}
};

magija operator*(magija a, magija b){
  magija c;
  FOR(i,-200,201) FOR(j,-200,201) if (i+j >= -200 && i+j <= 200) c[i+j] += a[i]*b[j];
  return c;
}

int n, k;
double p[205];

magija pref[205], suff[205];

void solve(){
  
  cin >> n >> k;
  REP(i,n) cin >> p[i];
  sort(p, p+n);
  pref[0][0] = suff[0][0] = 1;

  REP(i,n){
    magija temp;
    temp[1] = p[i];
    temp[-1] = 1-p[i];
    pref[i+1] = pref[i] * temp;
  }

  REP(i,n){
    magija temp;
    temp[1] = p[n-1-i];
    temp[-1] = 1-p[n-1-i];
    suff[i+1] = suff[i] * temp;
  }

  double r = 0;
  REP(i,k+1){
    magija temp = pref[i] * suff[k-i];
    r = max(r, temp[0]);
  } cout << fixed << setprecision(10) << r << endl;
  
}

int main(){

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", TRACE(i), solve();

  return 0;
}
