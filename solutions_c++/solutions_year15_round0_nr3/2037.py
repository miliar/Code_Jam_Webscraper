#include <iostream>
#include <string>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::min;

enum Value {E, I, J, K};
int SIGN[4][4] = {
  {1, 1, 1, 1},
  {1, -1, 1, -1},
  {1, -1, -1, 1},
  {1, 1, -1, -1}
};
static int MULT[4][4] = {
  {E, I, J, K},
  {I, E, K, J},
  {J, K, E, I},
  {K, J, I, E}
};

struct Quaternion {
  Quaternion(int s=1, Value v=E): sign(s), value(v) { }
  int sign;
  Value value;
};

bool operator==(Quaternion const &q1, Quaternion const &q2) {
  return q1.sign == q2.sign && q1.value == q2.value;
}

bool operator!=(Quaternion const &q1, Quaternion const &q2) {
  return q1.sign != q2.sign || q1.value != q2.value;
}

Quaternion operator*(Quaternion const &q1, Quaternion const &q2) {
  return Quaternion(q1.sign * q2.sign * SIGN[q1.value][q2.value],
                    (Value)MULT[q1.value][q2.value]);
}

Quaternion pow(Quaternion const &q, int k) {
  Quaternion r(1, E);
  while (k--) {
    r = r * q;
  }
  return r;
}

Quaternion from_char(char ch) {
  Quaternion q;
  q.sign = 1;
  if (ch == 'i') {
    q.value = I;
  } else if (ch == 'j') {
    q.value = J;
  } else {
    q.value = K;
  }
  return q;
}


void solve_case(int case_id) {
  int l; cin >> l;
  long long x; cin >> x;
  string s; cin >> s;

  vector<Quaternion> left(l);
  for (int i = 0; i < l; ++i) {
    left[i] = (i == 0) ? from_char(s[0]) : left[i-1] * from_char(s[i]);
  }
  vector<Quaternion> right(l);
  for (int i = l-1; i >= 0; --i) {
    right[i] = (i == l-1) ? from_char(s[i]) : from_char(s[i]) * right[i+1];
  }

  Quaternion full = pow(left[l-1], x);
  if (full != Quaternion(-1, E)) {
    cout << "Case #" << case_id << ": NO\n";
    return;
  }

  int left_i = 5 * l;
  auto val_i = Quaternion(1, I);
  for (int i = 0; i < l; ++i) {
    if (left[i] == val_i) {
      left_i = min(left_i, i);
    } if (x > 1 && left[l-1] * left[i] == val_i) {
      left_i = min(left_i, l + i);
    } if (x > 2 && pow(left[l-1], 2) * left[i] == val_i) {
      left_i = min(left_i, 2*l + i);
    } if (x > 3 && pow(left[l-1], 3) * left[i] == val_i) {
      left_i = min(left_i, 3*l + i);
    }
  }

  int right_k = 5 * l;
  auto val_k = Quaternion(1, K);
  for (int i = 0; i < l; ++i) {
    if (right[l - i - 1] == val_k) {
      right_k = min(right_k, i);
    } if (x > 1 && right[l - i - 1] * right[0] == val_k) {
      right_k = min(right_k, l + i);
    } if (x > 2 && right[l - i - 1] * pow(right[0], 2) == val_k) {
      right_k = min(right_k, 2*l + i);
    } if (x > 3 && right[l - i - 1] * pow(right[0], 3) == val_k) {
      right_k = min(right_k, 3*l + i);
    }
  }

  // cout << " -- "  << left_i << " " << right_k << endl;

  if (left_i == 5*l || right_k == 5*l) {
    cout << "Case #" << case_id << ": NO\n";
    return;
  }

  if (left_i + right_k + 2 > x*l) {
    cout << "Case #" << case_id << ": NO\n";
    return;
  }

  cout << "Case #" << case_id << ": YES\n";  
}

int main() {
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    solve_case(i);
  }
  return 0;
}
