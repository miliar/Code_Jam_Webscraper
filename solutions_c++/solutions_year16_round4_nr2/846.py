#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef pair<int,ii> iii;

const int maxn = 210;
ld pro[maxn][maxn];
ld p[maxn];
int n,k;

int main(){
  cout.precision(10);
  cout.setf(ios::fixed);
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> n >> k;
    for(int i = 0; i < n; ++i) cin >> p[i];
    ld sol = 0.0;
    for(int masc = 0; masc < (1<<n); ++masc){
      int c = 0;
      for(int i = 0; i < n; ++i) if(masc&(1<<i)) ++c;
      if(c != k) continue;
      memset(pro,0,sizeof(pro));
      pro[0][0] = 1.0;
      int x = 0;
      for(int i = 0; i < k; ++i){
	while(!(masc&(1<<x))) ++x;
	pro[i+1][0] = (1.0-p[x])*pro[i][0];
	for(int j = 1; j <= k; ++j){
	  pro[i+1][j] = p[x]*pro[i][j-1]+(1.0-p[x])*pro[i][j];
	}
	++x;
      }
      sol = max(sol,pro[k][k/2]);
    }
    cout << "Case #" << cass << ": " << sol << '\n';
  }
}