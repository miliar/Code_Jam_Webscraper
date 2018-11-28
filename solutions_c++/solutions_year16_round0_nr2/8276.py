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

map<pair<char, string>, int> CACHE;

string flip(const string& pancakes, int depth) {
  string result = pancakes;

  for (int i = 0; i < depth / 2; ++i)
    swap(result[i], result[depth - i - 1]);
  for (int i = 0; i < depth; ++i) {
    if (result[i] == '-')
      result[i] = '+';
    else
      result[i] = '-';
  }

  return result;
}

int solve(const string& pancakes, char rr) {
  if (pancakes.empty())
    return 0;
  if (pancakes.size() == 1 && pancakes[0] == rr)
    return 0;
  if (pancakes.size() == 1 && pancakes[0] != rr)
    return 1;

  auto it = CACHE.find(make_pair(rr, pancakes));
  if (it != CACHE.end())
    return (*it).second;

  if (pancakes.back() == rr) {
    string pp(pancakes.begin(), pancakes.begin() + pancakes.size() - 1);
    int result = solve(pp, rr);

    CACHE.insert(make_pair(make_pair(rr, pancakes), result));

    return result;
  } else {
    int result = 0;

    char not_rr = '-';
    if (rr == '-')
      not_rr = '+';

    string pp(pancakes.begin(), pancakes.begin() + pancakes.size() - 1);
    result = 1 + solve(pp, not_rr);

    string f = flip(pancakes, pancakes.size());
    if (f != pancakes && f.back() == rr) {
      int r2 = 1 + solve(f, rr);
      if (result > r2) {
        result = r2;
      }
    }

    CACHE.insert(make_pair(make_pair(rr, pancakes), result));

    return result;
  }
}

int main(int argc, char* argv[]) {
  ifstream in_file("B-large.in");
  ofstream out_file("out.txt");

  int test_cases = 0;
  in_file >> test_cases;

  for (int case_index = 0; case_index < test_cases; ++case_index) {
    print_result(out_file, "Case #", case_index + 1, ": ");

    string pancakes;
    in_file >> pancakes;

    CACHE.clear();

    int result = solve(pancakes, '+');

    print_result(out_file, result, "\n");
  }
}