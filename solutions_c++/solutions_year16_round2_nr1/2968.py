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
vector<int> ToDigits(T t, int r = 10) {
  vector<int> result;

  while (t) {
    result.push_back(t % r);
    t /= r;
  }

  reverse(result.begin(), result.end());

  return result;
}

template<typename T>
T FromDigits(const vector<int>& digits, int r = 10) {
  T result = 0;

  for (size_t i = 0; i < digits.size(); ++i) {
    result *= r;
    result += digits[i];
  }

  return result;
}

template<typename T>
T FindFactor(T t) {
  for (T i = 2; i * i <= t; ++i) {
    if (t % i == 0)
      return i;
  }

  return t;
}

template<typename T>
ostream& operator<<(ostream& s, const vector2d<T>& c) {
  size_t max_number_size = 2;
  for (size_t i = 0; i < c.size1(); ++i) {
    auto r = ToDigits(i, 10);
    max_number_size = max(max_number_size, r.size() + 1);

    for (size_t j = 0; j < c.size2(); ++j) {
      r = ToDigits(j, 10);
      max_number_size = max(max_number_size, r.size() + 1);

      r = ToDigits(c(i, j), 10);
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

  vector<pair<char, string>> known;
  known.push_back(make_pair('Z', "ZERO"));
  known.push_back(make_pair('W', "TWO"));
  known.push_back(make_pair('U', "FOUR"));
  known.push_back(make_pair('X', "SIX"));
  known.push_back(make_pair('G', "EIGHT"));
  known.push_back(make_pair('O', "ONE"));
  known.push_back(make_pair('R', "THREE"));
  known.push_back(make_pair('F', "FIVE"));
  known.push_back(make_pair('V', "SEVEN"));
  known.push_back(make_pair('N', "NINE"));

  vector<int> known_number(10);
  known_number[0] = 0;
  known_number[1] = 2;
  known_number[2] = 4;
  known_number[3] = 6;
  known_number[4] = 8;
  known_number[5] = 1;
  known_number[6] = 3;
  known_number[7] = 5;
  known_number[8] = 7;
  known_number[9] = 9;

  for (int case_index = 0; case_index < test_cases; ++case_index) {
    vector<int> N(10);

    print_result(out_file, "Case #", case_index + 1, ": ");

    string S;
    in_file >> S;

    int i = 0;
    while (i < 10) {
      if (S.find(known[i].first) != string::npos) {
        ++N[known_number[i]];

        for (size_t j = 0; j < known[i].second.size(); ++j) {
          auto p = S.find(known[i].second[j]);
          if (p != string::npos)
            S.erase(S.begin() + p);
        }
      } else {
        ++i;
      }
    }

    for (int i = 0; i < 10; ++i) {
      for (int j = 0; j < N[i]; ++j) {
        print_result(out_file, (char) ('0' + i));
      }
    }
    print_result(out_file, "\n");
  }
}