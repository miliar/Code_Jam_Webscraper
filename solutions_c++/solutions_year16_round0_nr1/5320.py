#include <cstring>
#include <fstream>
#include <string>
using namespace std;

bool allSeen(bool * digits) {
  for (int i = 0; i < 10; ++i) {
    if (!digits[i]) {
      return false;
    }
  }
  return true;
}

void setDigits(int n, bool * digits) {
  while (n) {
    digits[n % 10] = true;
    n /= 10;
  }
}

int getCount(int n) {
  bool digits[10];
  memset(digits, 0, sizeof(digits));
  int res = n;
  setDigits(n, digits);
  while (!allSeen(digits)) {
    res += n;
    setDigits(res, digits);
  }
  return res;
}

int main(int argc, char * argv[]) {
  ifstream ifs(argv[1]);
  ofstream ofs((string(argv[1]) + ".out").c_str());
  int t;
  ifs >> t;
  for (int i = 0; i < t; ++i) {
    int n;
    ifs >> n;
    ofs << "Case #" << (i + 1) << ": ";
    if (0 == n) {
      ofs << "INSOMNIA" << endl;
    } else {
      ofs << getCount(n) << endl;
    }
  }
  return 0;
}
