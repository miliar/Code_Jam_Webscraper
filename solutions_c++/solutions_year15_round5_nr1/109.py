#define NDEBUG
#include <climits>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

#define repeat(n) for (int repc = (n); repc > 0; --repc)
template<typename T, typename U> inline void makemin(T &res, const U &x) {
  if (x < res) {
    res = x;
  }
}
template<typename T, typename U> inline void makemax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}
typedef long long int64;
#define ZERO(v) memset((v), 0, sizeof (v))

vector<int> read_seq(int N) {
  int64 A0, M, C, R;
  cin >> A0 >> M >> C >> R;
  vector<int> ret;
  ret.push_back(A0);
  repeat (N-1) {
    ret.push_back((ret.back() * M + C) % R);
  }
  return ret;
}

int D;
const int MAX = 1000005;
vector<int> children[MAX+10];
int add[MAX+10], sub[MAX+10];

void rek(const vector<int> &S, int pos, int A, int B) {
  makemax(A, S[pos] - D);
  makemin(B, S[pos]);
  if (A <= B) {
    ++add[A];
    ++sub[B+1];
    for (int ch : children[pos]) {
      rek(S, ch, A, B);
    }
  }
}

int solve() {
  int N;
  cin >> N >> D;
  for (int i=0; i<N; ++i) {
    children[i].clear();
    if (children[i].capacity() > 100) {
      children[i].shrink_to_fit();
    }
  }
  ZERO(add);
  ZERO(sub);

  vector<int> S = read_seq(N);
  vector<int> M = read_seq(N);
  for (int i=1; i<N; ++i) {
    M[i] = M[i] % i;
    children[M[i]].push_back(i);
  }
  rek(S, 0, 0, INT_MAX);

  int ans = 0;
  int cnt = 0;
  for (int i=0; i<=MAX; ++i) {
    cnt += add[i];
    cnt -= sub[i];
    makemax(ans, cnt);
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %d\n", tt, solve());
    fflush(stdout);
  }
}
