#include <assert.h>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

template<typename T>
ostream& operator<<(ostream& s, const vector<T>& c);

template<typename T>
ostream& operator<<(ostream& s, const set<T>& c);

template<typename T, typename TT>
ostream& operator<<(ostream& s, const map<T, TT>& c);

template<typename T>
ostream& operator<<(ostream& s, const vector<T>& c) {
  cout << '[';
  size_t i = 0;
  for (auto it = c.begin(); it != c.end(); ++it) {
    cout << (*it);
    if (i + 1 < c.size())
      cout << ", ";
    ++i;
  }
  cout << ']';
  return s;
}

template<typename T>
ostream& operator<<(ostream& s, const set<T>& c) {
  cout << '{';
  size_t i = 0;
  for (auto it = c.begin(); it != c.end(); ++it) {
    cout << (*it);
    if (i + 1 < c.size())
      cout << ", ";
    ++i;
  }
  cout << '}';
  return s;
}

template<typename T, typename TT>
ostream& operator<<(ostream& s, const map<T, TT>& c) {
  cout << '{';
  size_t i = 0;
  for (auto it = c.begin(); it != c.end(); ++it) {
    cout << (*it).first << ": " << (*it).second;
    if (i + 1 < c.size())
      cout << ", ";
    ++i;
  }
  cout << '}';
  return s;
}

template<typename T>
class vector2d {
 public:
  vector2d() {
  }

  vector2d(size_t n, size_t m) : n_(n), m_(m), v_(n * m) {
  }

  size_t size1() const {
    return n_;
  }

  size_t size2() const {
    return m_;
  }

  const T& operator()(size_t i, size_t j) const {
    assert(i < size1());
    assert(j < size2());
    return v_[i * size2() + j];
  }

  T& operator()(size_t i, size_t j) {
    assert(i < size1());
    assert(j < size2());
    return v_[i * size2() + j];
  }

 private:
  size_t n_{0};
  size_t m_{0};
  vector<T> v_;
};

template<typename T>
vector<int> ToRadix(T t, int r = 10) {
  vector<int> result;

  while (t) {
    result.push_back(t % r);
    t /= r;
  }

  reverse(result.begin(), result.end());

  return result;
}

template<typename T>
ostream& operator<<(ostream& s, const vector2d<T>& c) {
  size_t max_number_size = 2;
  for (size_t i = 0; i < c.size1(); ++i) {
    auto r = ToRadix(i, 10);
    max_number_size = max(max_number_size, r.size() + 1);

    for (size_t j = 0; j < c.size2(); ++j) {
      r = ToRadix(j, 10);
      max_number_size = max(max_number_size, r.size() + 1);

      r = ToRadix(c(i, j), 10);
      max_number_size = max(max_number_size, r.size() + 1);
    }
  }

  for (size_t i = 0; i < c.size1(); ++i) {
    size_t ii = c.size1() - i - 1;

    s << setw(max_number_size) << ii;
    for (size_t j = 0; j < c.size2(); ++j)
      s << setw(max_number_size) << c(ii, j);
    s << endl;
  }

  s << setw(max_number_size) << "";
  for (size_t j = 0; j < c.size2(); ++j)
    s << setw(max_number_size) << j;

  return s;
}

template<typename T>
void print_result(ofstream& out, const T& result) {
  cout << result;
  out << result;
}

template<typename T1, typename T2>
void print_result(ofstream& out, const T1& t1, const T2& t2) {
  cout << t1 << t2;
  out << t1 << t2;
}

template<typename T1, typename T2, typename T3>
void print_result(ofstream& out, const T1& t1, const T2& t2, const T3& t3) {
  cout << t1 << t2 << t3;
  out << t1 << t2 << t3;
}

int main(int argc, char* argv[]) {
  ifstream in_file("A-large.in");
  ofstream out_file("out.txt");

  int test_cases = 0;
  in_file >> test_cases;

  for (int case_index = 0; case_index < test_cases; ++case_index) {
    print_result(out_file, "Case #", case_index + 1, ": ");

    int result;

    int N = 0;
    in_file >> N;

    if (N == 0) {
      print_result(out_file, "INSOMNIA", "\n");
      continue;
    }

    int I = 1;

    set<int> seen;
    while (true) {
      auto r = ToRadix(N * I, 10);
      for (auto i = 0; i < r.size(); ++i)
        seen.insert(r[i]);

      bool all = true;
      for (int i = 0; i <= 9; ++i) {
        if (seen.find(i) == seen.end()) {
          all = false;
          break;
        }
      }

      if (all) {
        print_result(out_file, N * I, "\n");
        break;
      }

      ++I;
    }
  }
}