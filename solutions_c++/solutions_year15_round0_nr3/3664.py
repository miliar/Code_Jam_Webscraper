#include <array>
using std::array;

#include <iostream>
using std::cin;
using std::cout;
using std::endl;
using std::ostream;

#include <initializer_list>
using std::initializer_list;

#include <vector>
using std::vector;

class Quaternion {
public:
  Quaternion(const array<int64_t, 4> &v) : values(v) {}
  Quaternion(const Quaternion &rhs) = default;
  virtual ~Quaternion() = default;
  Quaternion operator*(const Quaternion &rhs) {
    array<int64_t, 4> Q;
    Q[0] = (values[0] * rhs.values[0]) - (values[1] * rhs.values[1]) -
           (values[2] * rhs.values[2]) - (values[3] * rhs.values[3]);
    Q[1] = (values[1] * rhs.values[0]) + (values[0] * rhs.values[1]) -
           (values[3] * rhs.values[2]) + (values[2] * rhs.values[3]);
    Q[2] = (values[2] * rhs.values[0]) + (values[3] * rhs.values[1]) +
           (values[0] * rhs.values[2]) - (values[1] * rhs.values[3]);
    Q[3] = (values[3] * rhs.values[0]) - (values[2] * rhs.values[1]) +
           (values[1] * rhs.values[2]) + (values[0] * rhs.values[3]);
    return Quaternion(Q);
  }
  const Quaternion &operator*=(const Quaternion &rhs) {
    return *this = *this * rhs;
  }
  bool operator!=(const Quaternion &rhs) { return values != rhs.values; }
  friend ostream &operator<<(ostream &out, const Quaternion &rhs);

private:
  array<int64_t, 4> values;
};

ostream &operator<<(ostream &out, const Quaternion &rhs) {
  out << "{" << rhs.values[0] << ", " << rhs.values[1] << ", "
      << rhs.values[2] << ", " << rhs.values[3] << "}";
  return out;
}

int main() {
  array<int64_t, 4> negativeOne{{-1, 0, 0, 0}};
  array<int64_t, 4> one{{1, 0, 0, 0}};
  array<int64_t, 4> iQ{{0, 1, 0, 0}};
  array<int64_t, 4> jQ{{0, 0, 1, 0}};
  array<int64_t, 4> kQ{{0, 0, 0, 1}};
  int64_t numCases = -1;
  cin >> numCases;
  for (int64_t t = 1; t <= numCases; ++t) {
    cout << "Case #" << t << ": ";
    vector<Quaternion> qs, ls;
    int64_t L = -1, X = -1;
    cin >> L >> X;
    ls.reserve(L);
    //qs.reserve(L * X);
    Quaternion Q(one);
    for (int64_t i = 0; i < L; ++i) {
      char v;
      array<int64_t, 4> a({{0, 0, 0, 0}});
      cin >> v;
      v -= 'h';
      a[v] = 1;
      Q *= a;
      ls.push_back(Quaternion(a));
    }
    Quaternion QX = Q;
    for (int64_t i = 1; i < X; ++i) {
      QX *= Q;
    }
    if (L == 1 || L * X < 3) {
      cout << "NO" << endl;
      continue;
    } else if (QX != negativeOne) {
      cout << "NO" << endl;
      continue;
    }
    for (int64_t i = 0; i < X; ++i) {
      qs.insert(end(qs), begin(ls), end(ls));
    }
    while (qs[0] != iQ && qs.size() >= 3) {
      qs[0] *= qs[1];
      qs.erase(begin(qs) + 1);
    }
    if (qs.size() < 3) {
      cout << "NO" << endl;
      continue;
    }
    while (qs[1] != jQ && qs.size() >= 3) {
      qs[1] *= qs[2];
      qs.erase(begin(qs) + 2);
    }
    if (qs.size() < 3) {
      cout << "NO" << endl;
      continue;
    }
    while (qs[2] != kQ && qs.size() > 3) {
      qs[2] *= qs[3];
      qs.erase(begin(qs) + 3);
    }
    cout << (qs[2] != kQ ? "NO" : "YES") << endl;
  }
}
