#include <iostream>
#include <string>
#include <cassert>

using namespace std;

enum class QuantAbs {
  One = 0, I, J, K
};

enum class Sign : bool {
  Negative, Positive
};

struct Quaternion {
  Sign sign;
  QuantAbs value;

  static const Quaternion I;
  static const Quaternion J;
  static const Quaternion K;
  static const Quaternion One;

  Quaternion& operator *= (Quaternion const& rhs) {
    static Quaternion values[][4] = {{Quaternion::One, Quaternion::I, Quaternion::J, Quaternion::K},
				     {Quaternion::I, -Quaternion::One, Quaternion::K, -Quaternion::J},
				     {Quaternion::J, -Quaternion::K, -Quaternion::One, Quaternion::I},
				     {Quaternion::K, Quaternion::J, -Quaternion::I, -Quaternion::One}};
				    
    bool reverse_sign = (sign != rhs.sign);
    *this = values[int(value)][int(rhs.value)];
    if (reverse_sign)
      *this = -*this;
    return *this;
  }

  friend bool operator == (Quaternion const& lhs, Quaternion const& rhs) {
    return lhs.sign == rhs.sign && lhs.value == rhs.value;
  }

  friend bool operator != (Quaternion const& lhs, Quaternion const& rhs) {
    return !(lhs == rhs);
  }

  friend Quaternion operator* (Quaternion const& lhs, Quaternion const& rhs) {
    return Quaternion(lhs) *= rhs;
  }

  friend Quaternion operator -(Quaternion const& x) {
    return {x.sign == Sign::Negative ? Sign::Positive : Sign::Negative, x.value};
  }
};
const Quaternion Quaternion::I = {Sign::Positive, QuantAbs::I};
const Quaternion Quaternion::J = {Sign::Positive, QuantAbs::J};
const Quaternion Quaternion::K = {Sign::Positive, QuantAbs::K};
const Quaternion Quaternion::One = {Sign::Positive, QuantAbs::One};

Quaternion quant_from_char(char c) {
  QuantAbs value;
  switch (c) {
  case 'i': value = QuantAbs::I;break;
  case 'j': value = QuantAbs::J;break;
  case 'k': value = QuantAbs::K;break;
  default:
    assert(false && "Unexpected char");
    value = QuantAbs::I; break;
    break;
  }

  return {Sign::Positive, value};
}

bool solve(int repeats, string s) {
  Quaternion prod = {Sign::Positive, QuantAbs::One};
  bool seen_i = false;
  bool seen_k_after_i = false;
  bool last_is_minus_one = false;
  
  for (int repeat = 0; repeat < repeats; ++repeat) {
    for (char c : s) {
      prod *= quant_from_char(c);
      if (!seen_i){
	seen_i = prod == Quaternion::I;
	continue;
      }
      if (!seen_k_after_i) {
	seen_k_after_i = prod == Quaternion::K;
	continue;
      }
      last_is_minus_one = prod == -Quaternion::One;
    }
  }

  return seen_i && seen_k_after_i && last_is_minus_one;
}

int main() {
  int cases;
  cin >> cases;

  for (int n = 1; n <= cases; ++n) {
    int repeats;
    int dummy;
    string s;
    cin >> dummy >> repeats >> s;

    cout << "Case #" << n << ": " << (solve(repeats, s) ? "YES" : "NO") << "\n";
  }
}
