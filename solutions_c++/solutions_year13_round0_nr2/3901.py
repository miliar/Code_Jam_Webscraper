#include <algorithm>
#include <cstdio>

using namespace std;

namespace {

template<typename T, int N, int M>
struct static_2d {
  int n;
  int m;
  T array[N][M];

  static_2d() : n(0), m(0) { }
  static_2d(int n_, int m_) : n(n_), m(m_) { }

  void reset(const T &value) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        array[i][j] = value;
      }
    }
  }

  bool exists(const T &value) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (array[i][j] == value) return true;
      }
    }
    return false;
  }
};

typedef static_2d<int, 100, 100> input;
typedef static_2d<bool, 100, 100> scratch;

void mark(const input &this_input, scratch &buffer, int begin_x, int begin_y,
          int delta_x, int delta_y) {
  int iter_x = begin_x, iter_y = begin_y;

  int maximum = this_input.array[iter_x][iter_y];
  iter_x += delta_x;
  iter_y += delta_y;

  while (iter_x < this_input.n && iter_y < this_input.m) {
    maximum = max(maximum, this_input.array[iter_x][iter_y]);
    iter_x += delta_x;
    iter_y += delta_y;
  }

  iter_x = begin_x;
  iter_y = begin_y;

  while (iter_x < this_input.n && iter_y < this_input.m) {
    if (this_input.array[iter_x][iter_y] == maximum) {
      buffer.array[iter_x][iter_y] = true;
    }
    iter_x += delta_x;
    iter_y += delta_y;
  }
}

bool is_possible(const input &this_input) {
  scratch scratch_buffer(this_input.n, this_input.m);
  scratch_buffer.reset(false);

  for (int x = 0; x < this_input.n; x++) {
    mark(this_input, scratch_buffer, x, 0, 0, 1);
  }

  for (int y = 0; y < this_input.m; y++) {
    mark(this_input, scratch_buffer, 0, y, 1, 0);
  }

  return !scratch_buffer.exists(false);
}

void one_run(int case_num) {
  input this_input;
  scanf("%d %d", &this_input.n, &this_input.m);

  for (int i = 0; i < this_input.n; i++) {
    for (int j = 0; j < this_input.m; j++) {
      scanf("%d", &this_input.array[i][j]);
    }
  }

  printf("Case #%d: %s\n", case_num, is_possible(this_input) ? "YES":"NO");
}

}

int main() {
  int case_count = 0;
  scanf("%d", &case_count);

  for (int i = 0; i < case_count; i++) one_run(i + 1);

  return 0;
}
