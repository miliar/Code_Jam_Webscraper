using namespace std;
#include <algorithm>
#include <string.h>
#include <iostream>
#include <vector>

bool is_memo[500][500];
double memo[500][500];
double p[500];

double f(int i,int j){
  if ((j < 0) || (i < 0)) return 0;
  if (i + j == 0) return 1;
  if (is_memo[i][j]) return memo[i][j];
  double ans = (p[i] * f(i-1, j-1) + (1-p[i]) * f(i-1, j));
  is_memo[i][j] = true;
  memo[i][j] = ans;
  return ans;
}

int main(){
  int T;
  cin >> T;
  for (int t=1; t<=T; t++){

    int n,k;
    cin >> n >> k;
    vector<double> q;
    double tmp;
    for (int i=1; i<=n; i++){
      cin >> tmp;
      q.push_back(tmp);
    }
    sort(q.begin(), q.end());
    double best = 0.0;
    for (int br=0; br<=k; br++){
      for (int i=1; i<=br; i++){
        p[i] = q[i-1];
      }
      int len = q.size();

      for (int i=1; i<=k-br; i++){
        p[br + i] = q[len - i];
      }
      //if (best > -0.1) {
      //  cout << br << " " << best << endl;
      //  for (int i=1; i<=k; i++) cout << p[i] << " ";
      //  cout << endl;
      //  for (int i=0; i<n; i++) cout << q[i] << " ";
      //  cout << endl;
      //}
      best = max(best, f(k,k/2));
      memset(is_memo, 0, sizeof(is_memo));
      memset(memo, 0, sizeof(is_memo));
      memset(p, 0, sizeof(p));
    }
    
    //for (int i=0; i<n; i++) cout << q[i] << " ";
    //cout << endl;
    //for (int i=1; i<=k; i++) cout << p[i] << " ";
    //cout << endl;

    cout << "Case #" << t << ": " << best << endl;
    //
  }
}
