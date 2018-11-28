#include<cstdio>
#include<vector>
#include<iostream>

using namespace std;
#define f(i, a, n) for(int i = a; i < n; i++)
typedef long double ld;

int row[2][16];
int ans[2];

void read(int step) {
  cin >> ans[step]; ans[step]--;

  f(i, 0, 4) f(j, 0, 4){
    int x; cin >> x; x--;
    row[step][x] = i;
  }
}

void solve(){
  read(0); read(1);

  vector<int> assignment[4][4];
  f(i, 0, 16) assignment[row[0][i]][row[1][i]].push_back(i);
  vector<int> v = assignment[ans[0]][ans[1]];
  if (v.empty()) {
    cout << "Volunteer cheated!" << endl;
  } else if (v.size() > 1) {
    cout << "Bad magician!" << endl;
  } else {
    cout << v[0] + 1 << endl;
  }
}

int main(){
  int t; cin >> t;
  for(int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    solve();
  }
}
