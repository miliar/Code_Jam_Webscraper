#include <bits/stdtr1c++.h>
using namespace std;

typedef vector<int> vi;

//int g[50][50];
int l[100][50];
bool d[100];
int N, n;
bool pos[100];
//int g2[50][50];

bool f(int a, bool rc, bool fill, vector<vi> g) {
  if (a == n) {
    for (int i = 0; i < N+1; i++) {
      if (!pos[i]) {
        if (i < n) {
          for (int j = 0; j < n; j++)
            cout << " " << g[i][j];
        }
        else {
          for (int j = 0; j < n; j++)
            cout << " " << g[j][i-n];
        }
        break;
      }
    }
    cout << "\n";
    //for (int i = 0; i < N+1; i++)
    //  cout << pos[i] << " ";
    //cout << endl;
    //for (int i = 0; i < n; i++) {
    //  for (int j = 0; j < n; j++)
    //    cout << g[i][j] << " ";
    //  cout << endl;
    //}
    return true;
  }
  for (int i = 0; i < N; i++) {
    if (d[i])
      continue;
    //cout << "at " << a << " " << rc << " " << fill << ": " << i << " " << d[i] << endl;
    //for (int j = 0; j < n; j++) {
    //  for (int k = 0; k < n; k++)
    //    cout << " " << g[j][k];
    //  cout << endl;
    //}
    if (!rc) {
      bool v = true;
      for (int j = 0; j < n; j++) {
        if ((g[a][j] && g[a][j] != l[i][j]) || (a && g[a-1][j] >= l[i][j])) {
          v = false;
          break;
        }
      }
      if (v) {
        //memcpy(g2, g, sizeof g);
        vector<vi> g2(g);
        for (int j = 0; j < n; j++)
          g2[a][j] = l[i][j];
        d[i] = true;
        pos[a] = true;
        //cout << "done 1 " << a << " " << i << endl;
        if (f(a,true,fill,g2))
          return true;
        d[i] = false;
        pos[a] = false;
        //memcpy(g, g2, sizeof g);
      }
    }
    else {
      bool v = true;
      for (int j = 0; j < n; j++) {
        if ((g[j][a] && g[j][a] != l[i][j]) || (a && g[j][a-1] >= l[i][j])) {
          v = false;
          break;
        }
      }
      if (v) {
        //memcpy(g2, g, sizeof g);
        vector<vi> g2(g);
        for (int j = 0; j < n; j++)
          g2[j][a] = l[i][j];
        d[i] = true;
        pos[n+a] = true;
        //cout << "done 2 " << a << " " << i << endl;
        if (f(a+1,false,fill,g2))
          return true;
        d[i] = false;
        pos[n+a] = false;
        //memcpy(g, g2, sizeof g);
      }
    }
  }
  if (!fill) {
    //cout << " fill\n";
    if (!rc) {
      if (f(a,true,true,g))
        return true;
    }
    else {
      if (f(a+1,false,true,g))
        return true;
    }
  }
  return false;
}

int main() {
  ios::sync_with_stdio(0);
  int t; cin >> t;
  for (int T = 1; T <= t; T++) {
    //memset(g,0,sizeof g);
    memset(d,0,sizeof d);
    memset(pos,0,sizeof pos);
    cout << "Case #" << T << ":";
    cin >> n;
    N = 2*n-1;
    for (int i = 0; i < N; i++)
      for (int j = 0; j < n; j++)
        cin >> l[i][j];
    vector<vi> v;
    for (int i = 0; i < n; i++)
      v.push_back(vi(n,0));
    //cout << f(0,false,false,v) << endl;
    f(0,0,0,v);
  }
  return 0;
}
