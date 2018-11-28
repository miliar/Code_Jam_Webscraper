#include <sstream>
#include <iostream>
#include <string>

using namespace std;

int case_count;

// Gabriel wins -> true
bool f(int x, int r, int c) {
  if (x == 1) {
    return true;
  } else if (x == 2) {
    return (r * c) % 2 == 0;
  } else if (x == 3) {
    if (r == 1 || c == 1) {
      return false;
    } else{
      return (r * c) % 3 == 0;
    }
  } else if (x == 4) {
    if ((r * c) % 4 == 0) {
      return min(r, c) >= 3;
    } else {
      return false;
    }
  }
}

void work(int x, int r, int c) {
  if (f(x, r, c)) {
    cout << "Case #" << case_count << ": GABRIEL" << endl;
  } else {
    cout << "Case #" << case_count << ": RICHARD" << endl;
  }
}

int main() {
  string line;
  int T;
  int read = 0;
  case_count = 0;
  getline(cin, line);
  istringstream iss_outer(line);
  iss_outer >> T;
  while (T-- > 0) {
    // Read x, r, c
    int x, r, c;
    getline(cin, line);
    istringstream iss_inner1(line);
    iss_inner1 >> x >> r >> c;

    // Work on the data
    case_count++;
    work(x, r, c);
  }
  return 0;
}
