#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
int N;
ll X;
string s;

int val(char c) {
  return 1 + c - 'i';
}

struct Quat {
  static const int sign_[4][4];
  static const int car_[4][4];
  int sign, car;
  Quat operator * (const Quat &q) const {
    return {sign * q.sign * sign_[car][q.car], car_[car][q.car]};
  }
  Quat exp(ll e) {
    Quat r = {1, 0}, a = *this;
    while (e) {
      if (e & 1)
        r = r * a;
      e >>= 1;
      a = a * a;
    }
    return r;
  }
  bool operator == (const Quat &q) const {
    return sign == q.sign and car == q.car;
  }
  bool operator != (const Quat &q) const {
    return not (*this == q);
  }
};

const int Quat::sign_[4][4] = {1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1};
const int Quat::car_[4][4] = {0, 1, 2, 3, 1, 0, 3, 2, 2, 3, 0, 1, 3, 2, 1, 0};

bool solve() {
  ll T = min(4LL, X) * N;
  vector<Quat> F(T);
  for (int i = 0; i < T; ++i)
    F[i] = {1, val(s[i%N])};
  vector<Quat> R(F);
  for (int i = 1; i < T; ++i)
    F[i] = F[i-1] * F[i];
  for (int i = T-2; i >= 0; --i)
    R[i] = R[i] * R[i+1];
  if (F[N-1].exp(X) != Quat{-1, 0})
    return false;
  int a, b;
  for (a = 0; a < T; ++a)
    if (F[a] == Quat{1, 1})
      break;
  if (a == T)
    return false;
  for (b = 0; b < T; ++b)
    if (R[T-b-1] == Quat{1, 3})
      break;
  if (b == T)
    return false;
  b = N * X - b - 1;
  return a < b;
}

int main() {
  ios::sync_with_stdio(0);
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; ++i) {
    cin >> N >> X >> s;
    cout << "Case #" << i + 1 << ": ";
    cout << (solve() ? "YES" : "NO") << endl;
  }
  return 0;
}
