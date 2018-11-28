#include <iostream>
#include <cmath>
#include <sstream>
#include <string>

using namespace std;

bool ispalidrome(string numstr) {
  int startp = 0;
  int endp = numstr.length() - 1;
  while (startp <= endp) {
    if (numstr[startp] != numstr[endp]) return false;
    startp ++;
    endp--;
  }
  return true;
}

int fair_square(double si, double ei) {
  double sqei = sqrt(ei);
  double sqsi = sqrt(si);
  int minrt = static_cast<int>(ceil(sqsi));
  int maxrt = static_cast<int>(floor(sqei));
  // check all square numbers in the interval
  int nfairsquare = 0;
  for (int sqrnum = minrt; sqrnum <= maxrt; sqrnum++) {
    double sqnum = sqrnum * sqrnum;
    ostringstream convert, convertorigin;
    convert << sqnum;
    convertorigin << sqrnum;
    if (ispalidrome(convert.str()) && ispalidrome(convertorigin.str()))
      nfairsquare ++;
  }
  return nfairsquare;
}

int main(int argc, char** argv) {
  int T = 0;
  cin >> T;
  double si = 0, ei = 0; // start interval and end interval
  for (int i = 0; i < T; i++) {
    cin >> si >> ei;
    int ret = fair_square(si, ei);
    cout << "Case #" << i + 1 << ": " << ret << endl;
  }
  return 0;
}
