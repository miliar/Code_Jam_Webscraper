#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int K, N;
int P[256];
int t[256][25600];

vector<int> FindMembers() {
  memset(t, -1, sizeof(t));
  t[0][0] = 0;
  for (int i = 0; i < N; ++i) {
    int pos = P[i];
    for (int j = K; j >= 0; --j) {
      for (int k = 0; k <= j*100; ++k) {
	if (t[j][k] < 0) continue;
	if (t[j+1][k+pos] < 0) {
	  t[j+1][k+pos] = i;
	}
      }
    }
  }
  int min_k = -1;
  for (int k = 0; k <= K*100; ++k) {
    const int MID = K * 50;
    if (t[K][k] < 0) continue;
    // cout << k << " " << t[K][k] << endl;
    if (min_k < 0 || abs(k - MID) < abs(min_k - MID))
      min_k = k;
  }
  // cout << min_k << endl;
  vector<int> mem;
  int pos = min_k;
  for (int i = K; i > 0; --i) {
    int v = t[i][pos];
    mem.push_back(v);
    pos -= P[v];
  }
  return mem;
}

double Prob(const vector<int>& mem) {
  double sum[256][256] = {};
  sum[0][0] = 1;
  for (int i = 0; i < (int)mem.size(); ++i) {
    double p = P[mem[i]] / 100.0;
    for (int j = 0; j <= i+1; ++j) {
      if (j == 0) {
	sum[i+1][j] = sum[i][j] * (1-p);
      } else {
	sum[i+1][j] = sum[i][j] * (1-p) + sum[i][j-1] * p;
      }
    }
  }
  return sum[mem.size()][K/2];
}

double Solve() {
  // vector<int> mem = FindMembers();
  // for (int v : mem) {
  //   cout << v << " ";
  // }
  // return Prob(mem);

  double ans = 0;
  vector<int> used(N, 1);
  fill_n(used.begin(), N-K, 0);
  do {
    vector<int> mem;
    for (int i = 0; i < N; ++i) {
      if (used[i]) mem.push_back(i);
    }
    ans = max(ans, Prob(mem));
  } while(next_permutation(used.begin(), used.end()));
  return ans;
}

struct Comp {
  bool operator()(int a, int b) {
    return abs(a-50) > abs(b-50);
  }
};

int main() {
  int nnn;
  cin >> nnn;
  for (int iii = 0; iii < nnn; ++iii) {
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
      double p;
      cin >> p;
      P[i] = (int)(p * 100 + 0.5);
    }
    sort(P, P+N, Comp());
    cout.precision(8);
    cout << "Case #" << iii+1 << ": " << fixed << Solve() << endl;
  }
}
