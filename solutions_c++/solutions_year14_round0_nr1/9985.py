#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string runtest(istream &is) {
  int possible[16] = {0};

  for (int r = 0; r < 2; r++) {
    int row;
    is >> row;
    row--;
    is.ignore(1024, '\n');

    int i;
    for (i=0; i<row;i++) {
      is.ignore(1024, '\n');
    }

    int possiblenum;
    for (int j = 0; j < 4; j++) {
      is >> possiblenum;
      possible[possiblenum-1]++;
    }
    is.ignore(1024, '\n');

    i++;

    while (i<4) {
      is.ignore(1024, '\n');
      i++;
    }
  }

  int soln = 0;
  for (int i = 0; i < 16; i++) {
    if (possible[i] == 2) {
      // indicates a possible solution, but there should only be 1 if the magician did it right
      if (soln) {
        return "Bad magician!";
      } else {
        soln = i+1;
      }
    }
  }

  if (soln) {
    ostringstream ss;
    ss << soln;
    return ss.str();
  }

  return "Volunteer cheated!";

}

void testwrapper(istream &is) {
  int t;
  is >> t;

  for (int i = 0; i < t; i++) {
    cout << "Case #" << i+1 << ": " << runtest(is) << endl;
  }
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    cout << "Usage: a <infile>" << endl;
  }

  ifstream is(argv[1]);

  if (!is) {
    cerr << "Couldn't open input file." << endl;
    exit(1);
  }

  testwrapper(is);
}
