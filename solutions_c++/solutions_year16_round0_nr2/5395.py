#include <fstream>
#include <string>
using namespace std;
void flip(int i, string * stack) {
  for (; 0 <= i; --i) {
    (*stack)[i] = ('-' == (*stack)[i] ? '+' : '-');
  }
}
int getCount(string const & line) {
  string stack = line;
  int flips = 0;
  for (int i = stack.size() - 1; 0 <= i; --i) {
    if ('-' == stack[i]) {
      ++flips;
      flip(i, &stack);
    }
  }
  return flips;
}
int main(int argc, char * argv[]) {
  ifstream ifs(argv[1]);
  ofstream ofs((string(argv[1]) + ".out").c_str());
  int t;
  ifs >> t;
  string line;
  getline(ifs, line);
  for (int i = 0; i < t; ++i) {
    getline(ifs, line);
    ofs << "Case #" << (i + 1) << ": " << getCount(line) << endl;
  }
  return 0;
}
