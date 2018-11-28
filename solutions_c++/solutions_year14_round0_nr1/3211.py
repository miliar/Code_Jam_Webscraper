#include <iostream>
#include <iomanip>
#include <array>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

namespace std {
  template <typename T, size_t N>
  istream& operator>>(istream& in, array<T, N>& xs) {
    copy_n(istream_iterator<T>(in), N, xs.begin());
    return in;
  }

  template <typename T, size_t N>
  ostream& operator<<(ostream& out, array<T, N> const& xs) {
    out << "{";
    copy(xs.begin(), xs.end(), ostream_iterator<T>(out, ", "));
    out << "}";
    return out;
  }
}

// i is 1-based
array<int, 4> choose_row(istream& in, int i) {
  array<int, 4> r, rr;
  for (int j = 0; j < 4; ++j) {
    in >> r;
    if (j + 1 == i) {
      rr = r;
    }
  }
  return rr;
}

int main() {

  int T;
  cin >> T;

  for (int t = 0; t < T; ++t) {
    int c1, c2;

    cin >> c1;
    array<int, 4> r1(choose_row(cin, c1));
    sort(r1.begin(), r1.end());

    cin >> c2;
    array<int, 4> r2(choose_row(cin, c2));
    sort(r2.begin(), r2.end());

    vector<int> cards;
    set_intersection(r1.begin(), r1.end(), r2.begin(), r2.end(),
        back_inserter(cards));

    cout << "Case #" << (t + 1) << ": ";
    if (cards.empty()) {
      cout << "Volunteer cheated!";
    } else if (cards.size() > 1) {
      cout << "Bad magician!";
    } else {
      cout << cards.front();
    }
    cout << endl;
  }
}

