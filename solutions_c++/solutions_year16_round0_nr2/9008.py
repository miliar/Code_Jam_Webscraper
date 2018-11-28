#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <bitset>
#include <pthread.h>

using namespace std;

#define NDEBUG 1

#ifdef NDEBUG
  #define DEBUG(msg)
#else
  #define DEBUG(msg) cout << msg << endl;
#endif

void output_result(unsigned int result) {
  static int test = 1;
  cout << "Case #" << test << ": " << result << endl;
  test++;
}

string print_pattern(bool *pattern, int size) {
  string pat = "";
  for (int i=0; i < size; i++) {
    pat += (pattern[i] ? '+' : '-');
  }
  return pat;
}

#define status(happy) (happy ? '+' : '-')

int main (int argc, char **argv) {

  bool pattern[100];

  for (int i=0; i < 100; i++){
    // unhappy
    pattern[i] = false;
  }

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

  unsigned int number;
  unsigned int testcases;

  infile >> testcases;
  DEBUG("number of test cases is " << testcases);
  for (int test=1; test <= testcases; test++) {
    string line;

    do {
      getline(infile, line);
      if (infile.eof())
        exit(0);
    } while (line.empty());

    int pattern_size = 0;
    for_each(line.begin(), line.end(), [&] (char &c) {
      pattern[pattern_size] = (c == '-' ? false : true);
      pattern_size++;
    });
    DEBUG("pattern read " << print_pattern(pattern, pattern_size));

    // Remove ending unhappy, they will become happy after the last flip
    int end = pattern_size - 1;
    for (; end >=0 && !pattern[end]; end--)
    ;

    DEBUG("considering " << end << " pancakes");

    if (pattern_size == 1) {
      output_result(pattern[0] ? 0 : 1);
      continue;
    }

    int flips = 0;
    bool all_happy = pattern[0];
    for (int i=1; i <= end; i++) {
      DEBUG("pattern was " << status(all_happy));
      bool is_happy = pattern[i];
      DEBUG("pattern is going " << status(is_happy));
      if (all_happy && !is_happy) {
        DEBUG("then flip");
        all_happy = !all_happy;
        flips++;
        continue;
      }
      if (!all_happy && is_happy) {
        DEBUG("then flip");
        all_happy = !all_happy;
        flips++;
        continue;
      }
    }
    // Last flip
    int last_flips;

    bool bottom_happy = pattern[pattern_size - 1];
    bool top_happy = pattern[end];
    if (top_happy && bottom_happy)
      last_flips = 0;
    else if (!top_happy && bottom_happy)
      last_flips = 1;
    else if (top_happy && !bottom_happy)
      last_flips = 2;
    else // (!top_happy && !bottom_happy)
      last_flips = 1;
    output_result(flips + last_flips);
  }

  infile.close();
  return 0;
}
