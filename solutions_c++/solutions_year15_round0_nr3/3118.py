#include <iostream>
#include <cstdlib>
#include <cstddef>
#include <string>
#include <vector>

using namespace std;

enum class Unit { L = 0, I = 1, J = 2, K = 3 };

using pair_t = pair<bool, Unit>;
using vector_t = vector<pair_t>;
using matrix_t = vector<vector_t>;

matrix_t build_matrix() {
  matrix_t m;
  vector_t v;
  v.push_back({true, Unit::L});
  v.push_back({true, Unit::I});
  v.push_back({true, Unit::J});
  v.push_back({true, Unit::K});
  m.push_back(v);
  v.clear();
  v.push_back({true, Unit::I});
  v.push_back({false, Unit::L});
  v.push_back({true, Unit::K});
  v.push_back({false, Unit::J});
  m.push_back(v);
  v.clear();
  v.push_back({true, Unit::J});
  v.push_back({false, Unit::K});
  v.push_back({false, Unit::L});
  v.push_back({true, Unit::I});
  m.push_back(v);
  v.clear();
  v.push_back({true, Unit::K});
  v.push_back({true, Unit::J});
  v.push_back({false, Unit::I});
  v.push_back({false, Unit::L});
  m.push_back(v);
  return m;
};

const matrix_t matrix = build_matrix();

pair_t operator*(const Unit &a, const pair_t &b) {
  auto res = matrix[(size_t)a][(size_t)b.second];
  res.first = res.first == b.first;
  return res;
}

pair_t operator*(const pair_t &a, const Unit &b) {
  auto res = matrix[(size_t)a.second][(size_t)b];
  res.first = res.first == a.first;
  return res;
}

pair_t operator*(const pair_t &a, const pair_t &b) {
  auto res = matrix[(size_t)a.second][(size_t)b.second];
  res.first = (res.first == b.first) == a.first;
  return res;
}

bool process(size_t len, size_t n, const string &nums) {
  if (len != nums.size()) {
    cout << "Error: the string is not of the expected length!" << endl;
    exit(-1);
  }
  const size_t N = len * n;
  if (N < 3)
    return false;

  vector<Unit> v;
  for (auto &x : nums)
    switch (x) {
      case 'i':
        v.push_back(Unit::I);
        break;
      case 'j':
        v.push_back(Unit::J);
        break;
      case 'k':
        v.push_back(Unit::K);
        break;
      default:
        cout << "Error: unrecognized letter '" << x << "' found." << endl;
        exit(-1);
    }

  vector<Unit> w(N);
  {
    auto it = begin(w);
    for (size_t i = 0; i < n; i++)
      it = copy(begin(v), end(v), it);
  }

  vector<bool> end_i(N), start_k(N);

  const pair_t l_val = {true, Unit::L};
  const pair_t i_val = {true, Unit::I};
  const pair_t j_val = {true, Unit::J};
  const pair_t k_val = {true, Unit::K};

  pair_t x = l_val;
  {
    auto it_i = begin(end_i);
    for (auto it = begin(w); it != end(w); ++it)
      *(it_i++) = ((x = x * *it) == i_val);
  }

  x = l_val;
  {
    auto it_k = start_k.rbegin();
    for (auto it = w.rbegin(); it != w.rend(); ++it)
      *(it_k++) = (x = *it * x) == k_val;
  }

  for (size_t i = 0; i < N - 2; ++i)
    if (end_i[i]) {
      x = l_val;
      for (size_t j = i + 1; j < N - 1; ++j) {
        x = x * w[j];
        if (x == j_val and start_k[j + 1])
          return true;
      }
    }

  return false;
}

int main(int argc, const char **argv) {
  size_t t, l, x;
  string nums;
  cin >> t;
  size_t i = 0;
  while (t--) {
    cin >> l >> x;
    cin >> nums;

    bool result = process(l, x, nums);

    i++;
    cout << "Case #" << i << ": " << (result ? "YES" : "NO") << endl;
  }
  return EXIT_SUCCESS;
}
