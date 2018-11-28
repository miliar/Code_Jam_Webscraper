#include <iostream>
using namespace std;

enum quat { E, I, J, K };

quat mul(quat a, quat b) {
  if (a == E) return b;
  if (a == I) {
    if (b == J) return K;
    if (b == K) return J;
    return E;
  }
  if (a == J) {
    if (b == I) return K;
    if (b == K) return I;
    return E;
  }
  if (b == I) return J;
  if (b == J) return I;
  return E;
}

bool sign(quat a, quat b) {
  return (a == b) or (a == I and b == K) or (a == J and b == I) or (a == K and b == J);
}

quat conv(char x) {
  if (x == 'i') return I;
  if (x == 'j') return J;
  if (x == 'k') return K;
  return E;
}

inline bool solve() {
  int L; long long int X; cin >> L >> X;
  string S; cin >> S;
  quat s = E; bool sig = false;
  for (char c : S) {
    sig = sig xor sign(s, conv(c));
    s = mul(s, conv(c));
  }
  if (not ((s == E and sig and X%2 == 1) or (s != E and X%4 == 2))) return false;
  s = E; sig = false;
  bool step1 = false, step2 = false;
  for (int i = 0; i < min(8LL, X); ++i) {
    for (char c : S) {
      sig = sig xor sign(s, conv(c));
      s = mul(s, conv(c));
      if (s == I and not sig) step1 = true;
      if (step1 and s == K and not sig) step2 = true;
    }
  }
  return step2;
}

int main() {
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    cout << "Case #" << cas << ": " << (solve() ? "YES" : "NO") << endl;
  }
}