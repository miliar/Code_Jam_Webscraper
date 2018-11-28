#include <vector>
#include <iostream>
#include <fstream>
#include <array>

template<class T>
struct mat_t {

  mat_t(size_t rows, size_t columns, T value = T())
    : rows_(rows)
    , columns_(columns)
    , impl(rows * columns, value)
  {}

  mat_t(mat_t const& other)
    : rows_(other.rows_)
    , columns_(other.columns_)
    , impl(other.impl)
  {}

  T & operator()(size_t row, size_t column)
  {
    return impl[row * columns_ + column];
  }

  size_t rows() const { return rows_; }
  size_t columns() const { return columns_; }

private:
  size_t rows_;
  size_t columns_;
  std::vector<T> impl;
};

mat_t<size_t> read_matrix(std::istream & stream)
{
  size_t rows, columns;
  stream >> rows >> columns;
  mat_t<size_t> m(rows, columns);
  for(size_t i = 0; i < rows; ++i) {
    for(size_t j = 0; j < columns; ++j) {
      size_t tmp;
      stream >> tmp;
      m(i,j) = tmp - 1;
    }
  }
  return m;
}

static const size_t MAX_VALUE = 100;


int main(int argc, char *argv[]) {
  std::ifstream fin(argv[1]);
  size_t count;
  fin >> count;
  std::vector<std::array<size_t, MAX_VALUE> > ver(100);
  std::vector<std::array<size_t, MAX_VALUE> > hor(100);
  for(size_t i = 1; i <= count; ++i) {
    for(auto & a : ver) {
      a.fill(0);
    }
    for(auto & a : hor) {
      a.fill(0);
    }
    auto answer = [&]() {
      mat_t<size_t> m = read_matrix(fin);
    
      for(size_t i = 0; i < m.rows(); ++i) {
        for(size_t j = 0; j < m.columns(); ++j) {
          for(size_t k = m(i,j); k < MAX_VALUE; ++k) {
            hor[i][k]++;
            ver[j][k]++;
          }
        }
      }
      for(size_t i = 0; i < m.rows(); ++i) {
        for(size_t j = 0; j < m.columns(); ++j) {
          size_t k = m(i,j);
          if ((hor[i][k] != m.columns()) && (ver[j][k] != m.rows())) {
            return false;
          }
        }
      }
      return true;
    }();
    std::cout << "Case #" << i << ": " << (answer ? "YES" : "NO") << std::endl;
  }
}
