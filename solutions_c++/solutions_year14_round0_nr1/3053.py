#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <cassert>

using namespace std;

template<class T>
struct vec2 : private vector<T> {
  using size_type = typename vector<T>::size_type;
  using reference = typename vector<T>::reference;
  using const_reference = typename vector<T>::const_reference;

  vec2(size_type rows, size_type cols, const_reference val)
    : vector<T>(rows * cols, val)
    , rows_(rows)
    , cols_(cols)
  {
  }

  reference operator()(size_type x, size_type y) {
    assert(x < rows_ && y < cols_);
    return (*this)[x * rows_ + y];
  }

  const_reference operator()(size_type x, size_type y) const {
    assert(x < rows_ && y < cols_);
    return (*this)[x * rows_ + y];
  }

  size_type columns() const {
    return cols_;
  }

  size_type rows() const {
    return rows_;
  }

private:
  size_type rows_;
  size_type cols_;
};

string solve(vec2<int> const & field1, int row1, vec2<int> const& field2, int row2) {
  auto get_elems = [](vec2<int> const & fld, int row) {
    std::set<int> items;
    for (int y = 0; y < fld.columns(); ++y) {
      items.insert(fld(row, y));
    }
    return items;
  };

  std::set<int> items1 = get_elems(field1, row1);
  std::set<int> items2 = get_elems(field2, row2);

  std::vector<int> both;
  set_intersection(items1.begin(), items1.end(), items2.begin(), items2.end(),
      std::back_inserter(both));


  ostringstream os;

  if (both.size() == 1)
     os << *both.begin();
  else if (both.size() > 1)
    os << "Bad magician!";
  else
    os << "Volunteer cheated!";

  return os.str();
}

int main() {
  istream_iterator<int> is(std::cin);

  int n = *is++;

  for (int test_case = 0; test_case < n; ++test_case) {

    auto read_field = [&is]() {
      vec2<int> field(4, 4, 0);
      for (int x = 0; x < 4; ++x) {
        for (int y = 0; y < 4; ++y) {
          field(x, y) = *is++;
        }
      }
      return field;
    };


    int row1 = *is++ - 1;
    vec2<int> field1 = read_field();

    int row2 = *is++ - 1;
    vec2<int> field2 = read_field();

    std::cout
      << "Case #" << (test_case + 1) << ": "
      << solve(field1, row1, field2, row2)
      << "\n";
  }
}
