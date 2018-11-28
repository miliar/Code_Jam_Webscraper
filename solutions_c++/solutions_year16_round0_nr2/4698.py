#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
using namespace std;

map <string, int> mp;
string target;

void dfs(string str, int step){
  mp[str] = step;
  for (int i = 0; i < str.size(); i++){
    string now;
    for (int j = 0; j <= i; j++)
      now += "+-"[str[i-j]=='+'];
    for (int j = i + 1; j < str.size(); j++)
      now += str[j];
    if (mp.find(now) == mp.end()) dfs(now, step + 1);
    else if (mp[now] > step + 1) dfs(now, step + 1);
  }
}

int brute(string str){
  mp.clear();
  target = "";
  for (int i = 0; i < str.size(); i++) target += '+';
  dfs(str, 0);
  return mp[target];
}

int f[200][200], g[200][200];
int u[200][200], v[200][200];

int gao(string str){
  memset(f, 0, sizeof(f));
  memset(g, 0, sizeof(g));
  memset(u, 0, sizeof(u));
  memset(v, 0, sizeof(v));
  int n = str.size();
  //cout << str << ' ' << n << endl;
  for (int i = 0; i < n; i++){
    if (str[i] == '-') f[i][i] = u[i][i] = 1;
    else g[i][i] = v[i][i] = 1;
  }
  for (int k = 1; k < n; k++){
    for (int i = 0; i + k < n; i++){
      int j = i + k;
      f[i][j] = g[i][j] = u[i][j] = v[i][j] = 1e8;
      for (int s = i; s < j; s++){
        f[i][j] = min(f[i][j], g[i][s] + v[s+1][j] + 1);
        g[i][j] = min(g[i][j], f[i][s] + u[s+1][j] + 1);
        u[i][j] = min(u[i][j], g[i][s] + v[s+1][j]+ 1);
        v[i][j] = min(v[i][j], f[i][s] + u[s+1][j] + 1);
        if (f[s+1][j] == 0) f[i][j] = min(f[i][j], f[i][s]);
        if (g[s+1][j] == 0) g[i][j] = min(g[i][j], g[i][s]);
        if (u[i][s] == 0) u[i][j] = min(u[i][j], u[s+1][j]);
        if (v[i][s] == 0) v[i][j] = min(v[i][j], v[s+1][j]);
      }
    }
  }
  //for (int i=0; i < n; i++) cout << f[0][i] << ' ';
  //cout << endl;
  return f[0][n-1];
}

int main(){
  int t; cin >> t;
  for (int cas = 1; cas <= t; cas++){
    string str; cin >> str;
    int ret = gao(str);
    //int ret = brute(str);
    cout << "Case #" << cas << ": " << ret << endl;
  }
  return 0;
}
