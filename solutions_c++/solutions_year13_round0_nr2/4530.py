#include <iostream>
#include <vector>

class LawnSquare {
  public:
  int npos;
  int mpos;
  int height;

  bool operator<(const LawnSquare &rhs) const {
    return this->height < rhs.height;
  }
};

bool canMow (std::vector<int> squares, int height) {
  for (std::vector<int>::iterator it = squares.begin(); it != squares.end(); it++) {
    if (*it != 100 && *it != height) {
      // we've already specifically mown this square at a taller height.
      // mowing over it would break the pattern.
      return false;
    }
  }
  return true;
}

bool executeTest(int n, int m, std::vector<std::vector<int> > pattern) {
  // make a maxheap to hold each square of unmown lawn, based on desired height
  std::vector<LawnSquare> unMown;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      LawnSquare sq;
      sq.npos = i;
      sq.mpos = j;
      sq.height = pattern[i][j];
      unMown.push_back(sq);
    }
  }

  make_heap(unMown.begin(), unMown.end());

  // keep 2 vectors to track the height that the rows and columns have been mown to.
  // initially at 100mm each.
  std::vector<int> mownRows(n, 100);
  std::vector<int> mownCols(m, 100);

  // keep track of the height we have mown our grass to.  initially all at 100mm
  std::vector<std::vector<int> > lawn(n, std::vector<int>(m, 100));

  // attempt mow each square of the pattern, from tallest to shortest
  while (!unMown.empty()) {
    LawnSquare toMow = unMown.front();
    pop_heap(unMown.begin(), unMown.end()); unMown.pop_back();


    // we can successfully mow this square if we can mow either its row or column.
    // we can mow a row or column so long as all squares in it are either unmown or
    // already mowed to our desired height.
    if (canMow(lawn[toMow.npos], toMow.height)) {
      // mark the square as mown
      lawn[toMow.npos][toMow.mpos] = toMow.height;
    } else {
      // check if we can mow the column
      std::vector<int> col;
      for (int i = 0; i < n; i++) {
        col.push_back(lawn[i][toMow.mpos]);
      }
      if (canMow(col, toMow.height)) {
        // mark the square as mown
        lawn[toMow.npos][toMow.mpos] = toMow.height;
      } else {
        return false;
      }
    }
  }

  return true;
}

int main (int argc, char *argv[]) {
  int tests;

  std::cin >> tests;

  for (int t = 1; t <= tests; t++) {
    // process this test case
    int n, m;
    std::cin >> n >> m;

    // read in the desired height pattern of the lawn squares
    std::vector<std::vector<int> > pattern;
    for (int i = 0; i < n; i++) {
      std::vector<int> row;
      for (int j = 0; j < m; j++) {
        int h;
        std::cin >> h;
        row.push_back(h);
      }
      pattern.push_back(row);
    }

    bool result = executeTest(n, m, pattern);
    std::cout << "Case #" << t << ": ";
    if (result) {
      std::cout << "YES" << std::endl;
    } else {
      std::cout << "NO" << std::endl;
    }
  }
}
