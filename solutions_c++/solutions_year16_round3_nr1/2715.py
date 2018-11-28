#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <assert.h>

using namespace std;

#define NDEBUG 1

#ifdef NDEBUG
  #define DEBUG(msg)
#else
  #define DEBUG(msg) cout << msg << endl;
#endif

void output_result(string result) {
  static int test = 1;
  cout << "Case #" << test << ": " << result << endl;
  test++;
}

#define LETTER(n) (char)(n + 65)

int inroom(int senator[1000], int senators) {
  int n = 0;
  for (int i = 0; i < senators; ++i)
    n = senator[i] > 0 ? n + 1 : n;
  return n;
}

void solve_it(int senator[1000], int senators) {
  int major = 0;
  int minor = 1;
  string plan = "";
  while (inroom(senator, senators)) {
    for (int i=0; i<senators; i++) {
      if (senator[i] >= senator[major]) {
        minor = major;
        major = i;
      }
    }
    if (inroom(senator, senators) == 3 && senator[major] == 1 && senator[minor] == 1) {
      plan += LETTER(major);
      senator[major]--;
    } else {
      plan += LETTER(major);
      plan += LETTER(minor);
      senator[major]--;
      senator[minor]--;
    }
    plan += " ";
  }
  output_result(plan);
}

int main (int argc, char **argv) {

  if (argc < 1) {
    cout <<  "no input file" << endl;
    exit(1);
  }

  ifstream infile;
  char *testfile = argv[1];

  infile.open (testfile);
  if (!infile.is_open()) {
    cout << "cannot open file" << endl;
    exit(1);
  }

  unsigned int testcases;

  infile >> testcases;
  string line;
  getline(infile, line);
  DEBUG("number of test cases is " << testcases);
  for (int test=0; test < testcases; test++) {
    int parties;
    int senator[1000];
    string plan = "";

    int senators;
    infile >> senators;
    getline(infile, line);

    for (int i=0; i<senators; i++) {
      infile >> senator[i];
    }
    getline(infile, line);

    DEBUG("Senators read");
    for (int i=0; i<senators; i++) {
      DEBUG(senator[i] << "-");
    }

    solve_it(senator, senators);
  }

  infile.close();
  return 0;
}
