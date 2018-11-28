#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;
int T, N;
bool graph[1009][1009];
bool seen[1009];
int matchL[1009], matchR[1009];
int m, n;

bool bpm(int u) {
  for (int v=0; v<N; v++) if(graph[u][v]) {
    if(seen[v]) continue;
    seen[v] = true;
    
    if(matchR[v] < 0 || bpm(matchR[v])) {
      matchL[u] = v;
      matchR[v] = u;
      return true;
    }
  }
  return false;
}
int dwar(vector<double>& naomi, vector<double>& ken) {
  int res = 0;
  for (int i=0; i<N; ++i) {
    for (int j=0; j<N; ++j) {
      if(naomi[i] > ken[j]) {
        graph[i][j]=1;
      } else {
        graph[i][j]=0;
      }
    }
  }
  memset(matchL, -1, sizeof(matchL));
  memset(matchR, -1, sizeof(matchR));
  for (int i=0; i<N; ++i) {
    memset(seen, 0, sizeof(seen));
    if(bpm(i)) res++;
  }
  return res;
}

int war(vector<double>& naomi, vector<double>& ken) {
  int res = 0;
  for (int i=0; i<N; ++i) {
    for (int j=0; j<N; ++j) {
      if(naomi[i] < ken[j]) {
        graph[i][j]=1;
      } else {
        graph[i][j]=0;
      }
    }
  }
  memset(matchL, -1, sizeof(matchL));
  memset(matchR, -1, sizeof(matchR));
  for (int i=0; i<N; ++i) {
    memset(seen, 0, sizeof(seen));
    if(bpm(i)) res++;
  }
  return res;
}

int main() {
  freopen("inD.txt", "r", stdin);
  freopen("outD.txt", "w", stdout);
  cin >> T;
  for (int cases = 1; cases <= T; ++cases) {
    cout << "Case #" << cases << ": ";
    cin >> N;
    vector<double> ken(N), naomi(N);
    for (int i=0; i<N; ++i) cin >> naomi[i];
    for (int i=0; i<N; ++i) cin >> ken[i];
    
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    
    int r1 = dwar(naomi, ken);
    int r2 = war(naomi, ken);
    cout << r1 << " " << N-r2 << "\n";
  }
  return 0;
}