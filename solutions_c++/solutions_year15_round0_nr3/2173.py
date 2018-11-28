#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <fstream>
#include <string>

using namespace std;

enum Quaternion {O, I, J, K, _O, _I, _J, _K};
Quaternion MUL[4][4] = {
  {O,  I,  J,  K},
  {I, _O,  K, _J},
  {J, _K, _O,  I},
  {K,  J, _I, _O}
};

bool isNeg(Quaternion q) {
  return (q==_I || q==_J || q==_K || q==_O);
}

Quaternion getAbs(Quaternion q) {
  if (q==_I) return I;
  if (q==_J) return J;
  if (q==_K) return K;
  if (q==_O) return O;
  return q;
}

Quaternion getNeg(Quaternion q) {
  if (q==_I) return I;
  if (q==_J) return J;
  if (q==_K) return K;
  if (q==_O) return O;
  if (q==I) return _I;
  if (q==J) return _J;
  if (q==K) return _K;
  if (q==O) return _O;
  exit(-1);
}

Quaternion mul(Quaternion q1, Quaternion q2) {
  if (isNeg(q1) && isNeg(q2)) {
    return MUL[getAbs(q1)][getAbs(q2)];
  }
  if (!isNeg(q1) && !isNeg(q2)) {
    return MUL[q1][q2];
  }
  return getNeg(MUL[getAbs(q1)][getAbs(q2)]);
}

Quaternion getQ(char c) {
  switch (c) {
  case 'i':
    return I;
  case 'j':
    return J;
  case 'k':
    return K;
  }
  exit(-1);
}

bool doIt(const vector<Quaternion>& s) {
  vector<Quaternion> q;
  q.reserve(s.size());
  Quaternion cur = O;
  // dp
  for (int i=0; i<s.size(); i++) {
    cur = mul(cur, s[i]);
    q.push_back(cur);
  }

  // possible lasts
  vector<int> last; last.reserve(s.size());
  for (int i=0; i<q.size(); i++) {
    Quaternion third = getNeg(mul(q[i], q[q.size()-1]));
    if (third == K)
      last.push_back(i);
  }

  // N^2 checks (with opts)
  for (int i=0; i<q.size(); i++) {
    Quaternion first = q[i];
    if (first == I) {
      for (int j=int(last.size())-1; j>=0 && last[j] > i; j--) {
        int j_idx = last[j];
        Quaternion second = getNeg(mul(q[i], q[j_idx]));
        Quaternion third = getNeg(mul(q[j_idx], q[q.size()-1]));
        if (second == J && third == K) {
          return true;
        }
      }
    }
  }

  return false;
}

int main() {
  int tc, L, X;
  string s;
  cin >> tc;
  for (int t=1; t<=tc; t++) {
    cin >> L >> X;
    cin >> s;
    vector<Quaternion> Q;
    Q.reserve(L*X);
    for (int ii=0; ii<X; ii++) {
      for (int jj=0; jj<L; jj++) {
        Q.push_back( getQ( s[jj] ) );
      }
    }
    cout << "Case #"<<t<<": "<< (doIt(Q) ? "YES":"NO") << endl;
  }

  return 0;
}
