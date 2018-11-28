#include <iostream>
#include <string>
#include <cassert>
#include <stdexcept>

struct quat {
  unsigned int value;
  signed char sign;

  quat(unsigned char value, signed char sign) : value(value), sign(sign) {};
  explicit quat(char c) : sign (1) {
    switch(c) {
      case '1': value = 0; break;
      case 'i': value = 1; break;
      case 'j': value = 2; break;
      case 'k': value = 3; break;
      default: throw std::out_of_range("valid quaternion values are 1, i, j and k");
    }
  }
  
  quat operator-() const { return quat(value, -sign); }
  bool operator==(quat other) const { return other.value == this->value && other.sign == this->sign; }
  bool operator!=(quat other) const { return !(*this == other); }
  quat& operator*=(quat right);
  quat& operator/=(quat left);
  quat operator*(quat right) const { quat r = *this; return r *= right; }
  quat operator/(quat left) const { quat r = *this; return r /= left; }
  unsigned int hash() { return value + (sign > 0 ? 4 : 0); }
};

const quat O = quat(0,1);
const quat I = quat(1,1);
const quat J = quat(2,1);
const quat K = quat(3,1);

std::istream& operator>>(std::istream& in, quat& r) {
  std::istream::sentry s(in, true);
  if(!s) return in;
  char c;
  in >> c;
  try {
    r = quat(c);
  } catch (std::out_of_range) {
    in.setstate(std::ios::failbit);
  }
  return in;
}

std::ostream& operator<<(std::ostream& out, quat const& q) {
  if(q.sign < 0) out << "-";
  switch(q.value) {
    case 0: out << 1; break;
    case 1: out << "i"; break;
    case 2: out << "j"; break;
    case 3: out << "k"; break;
    default: out << "invalid quaternion"; break;
  }
  return out;
}

quat const mult_table[4][4] =
  {{O,  I,  J,  K}
  ,{I, -O,  K, -J}
  ,{J, -K, -O,  I}
  ,{K,  J, -I, -O}};

quat& quat::operator*=(quat right) {
  quat r = mult_table[this->value][right.value];
  this->value = r.value;
  this->sign *= r.sign * right.sign;
  return *this;
}

quat const div_table[4][4] =
  {{O, -I, -J, -K}
  ,{I,  O,  K, -J}
  ,{J, -K,  O,  I}
  ,{K,  J, -I,  O}};

quat& quat::operator/=(quat left) {
  quat r = div_table[this->value][left.value];
  this->value = r.value;
  this->sign *= r.sign * left.sign;
  return *this;
}

template <typename It>
quat product(It it, It const end) {
  quat r = O;
  for(;it != end; ++it) r *= quat(*it);
  return r;
}

template <typename It>
It find_value_substring(quat prefix, quat const val, It it, It stop, It const begin, It const end) {
  if(stop == begin) stop = end;
  do {
    if(it == end) it = begin;
    prefix *= quat(*it);
    if(prefix == val) return it;
    it++;
  } while(it != stop);
  return end;
}

bool solveable(std::string str, unsigned long rep) {
  quat str_product = product(str.begin(), str.end());

  int leftover = rep % 4;
  quat total_product = O;
  for(int i = 0; i < leftover; ++i) total_product *= str_product;
  if(total_product != -O) return false;
  
  std::string unit = str;
  if(rep > 1) unit+=str;
  if(rep > 2) unit+=str;
  if(rep > 3) unit+=str;
  assert((rep < 4 || product(unit.begin(), unit.end()) == O) && "invariant is false");
  std::string::iterator ilast = find_value_substring(O, I, unit.begin(), unit.end(), unit.begin(), unit.end());
  while(ilast != unit.end()) {
    std::string::iterator jlast = find_value_substring(O, J, ilast + 1, ilast + 1, unit.begin(), unit.end());
    while(jlast != unit.end()) {
      if(rep >= 4) return true;
      if(jlast > ilast) return true;
      if(rep == 3 && jlast < unit.begin() + str.length()) return true;
      jlast = find_value_substring(J, J, jlast + 1, ilast + 1, unit.begin(), unit.end());
    }
    ilast = find_value_substring(I, I, ilast + 1, unit.end(), unit.begin(), unit.end());
  }
  return false;
}

bool solveable_bruteforce(std::string str, unsigned long rep) {  
  quat str_product = product(str.begin(), str.end());

  int leftover = rep % 4;
  quat total_product = O;
  for(int i = 0; i < leftover; ++i) total_product *= str_product;
  if(total_product != -O) return false;

  std::string all = "";
  for(unsigned int i = 0; i < rep; ++i) all += str;
  std::string::iterator ilast = find_value_substring(O, I, all.begin(), all.end(), all.begin(), all.end());
  while(ilast != all.end()) {
    std::string::iterator jlast = find_value_substring(O, J, ilast + 1, all.end(), all.begin(), all.end());
    while(jlast != all.end()) {
      if(product(jlast + 1, all.end()) == K) return true;
      jlast = find_value_substring(J, J, jlast + 1, all.end(), all.begin(), all.end());
    }
    ilast = find_value_substring(I, I, ilast + 1, all.end(), all.begin(), all.end());
  }
  return false;
}

void table_check() {
  quat const quats[8] = { O, I, J, K, -O, -I, -J, -K };
  for(int i = 0; i < 8; ++i) {
    for(int j = 0; j < 8; ++j) {      
      bool ok = quats[i] * quats[j] / quats[i] == quats[j];
      if(!ok) {
	std::cout << "(1) Failed for: " << quats[i] << " * " << quats[j] << " / " << quats[i] << ": " << "\n";	
	std::cout << " = " << (quats[i] * quats[j]) << " / " << quats[i] << " = " << (quats[i] * quats[j] / quats[i]) << " = " << quats[j] << "\n";
      }
      ok = quats[i] * (quats[j] / quats[i]) == quats[j];
      if(!ok) std::cout << "(2) Failed for: " << quats[i] << " * " << quats[j] << "\n";	
    }
  }
}

int main() {
  table_check();

  int tests;
  std::cin >> tests;
  
  for(int i = 0; i < tests; ++i) {    
    unsigned long chars_unused, rep;
    std::cin >> chars_unused >> rep;

    std::string str;
    std::cin >> str;
   
    std::cout << "Case #" << (i + 1) << ": ";
    if(solveable(str, rep)) std::cout << "YES";
    else std::cout << "NO";
    std::cout << std::endl;    
  }

  return 0;
}
