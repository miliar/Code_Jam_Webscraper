#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef pair<int,ii> iii;

const int maxn = 30;
int n;
int mat[maxn][maxn];
int mat2[maxn][maxn];
int visti[maxn],vistj[maxn];
bool flag;

bool rell(int masc){
  for(int i = 0; i < n; ++i){
    for(int j = 0; j < n; ++j){
      if(masc&(1<<(n*i+j))){
	if(mat[i][j]) return false;
	mat2[i][j] = 1;
      }
      else mat2[i][j] = mat[i][j];
    }
  }
  return true;
}

bool check(int x){
  int c = 0;
  if(x == n) return true;
  for(int i = 0; i < n; ++i){
    if(visti[i]) continue;
    for(int j = 0; j < n; ++j){
      if(mat2[i][j] == 0 || vistj[j]) continue;
//       if(flag) cout << i << ' ' << j << endl;
      ++c;
      visti[i] = 1;
      vistj[j] = 1;
      if(check(x+1) == false) return false;
      visti[i] = 0;
      vistj[j] = 0;
    }
  }
  return c > 0;
}

int main(){
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    flag = (cass == 1);
    cin >> n;
    for(int i = 0; i < n; ++i){
      for(int j = 0; j < n; ++j){
	char c; cin >> c;
	if(c == '0') mat[i][j] = 0;
	else mat[i][j] = 1;
      }
    }
    int sol = n*n;
    for(int masc = 0; masc < (1<<(n*n)); ++masc){
      if(rell(masc) == false) continue;
//       if(cass == 1) cout << masc << endl;
      memset(visti,0,sizeof(visti));
      memset(vistj,0,sizeof(vistj));
      if(check(0)){
	int c = 0;
	for(int i = 0; i < n*n; ++i) if(masc&(1<<i)) ++c;
	sol = min(sol,c);
      }
    }
    cout << "Case #" << cass << ": " << sol << "\n";
  }
}