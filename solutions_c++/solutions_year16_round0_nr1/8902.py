#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <bitset>
#include <pthread.h>

using namespace std;

#define SEEN(number, n)  number |= (1 << n)
#define ALLSEEN(number) (number & 0x3FF) == 0x3FF

#ifdef NDEBUG
  #define DEBUG(msg)
#else
  #define DEBUG(msg) cout << msg << endl;
#endif

unsigned int results[100];

void output_results(int testcases) {
  for (int t=0; t < testcases; t++) {
    if (results[t] > 0)
      cout << "Case #" << t + 1 << ": " << results[t] << endl;
    else
      cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
  }
}

typedef struct solver_result {
  unsigned int number;
  unsigned int result_slot;
} solver_result;

void *solve_it(void *param) {
  unsigned int number = ((solver_result *)param)->number;
  unsigned int result_slot = ((solver_result *)param)->result_slot;

  // multiply the input
  DEBUG("testing  number " << number);

  unsigned int steps_to_goal = 0;
  unsigned int digits = 0;
  unsigned int counting = 0;
  for (unsigned int i = 1; ; i++) {

    if (number == 0)
      break;
    // compute the digits
    counting = number * i;
    DEBUG("counting digits for " << counting);
    for (unsigned int numbering=counting; numbering; numbering/=10) {
      int digit = numbering % 10;
      DEBUG("detected digit for number " << counting << " is " << (int)digit);
      SEEN(digits, digit);

      DEBUG("all seen so far=0b" << std::bitset<16>(digits));

      if (ALLSEEN(digits))
        break;
    }
    if (ALLSEEN(digits)) {
      DEBUG("all seen");
      steps_to_goal = counting;
      break;
    }
  }
  results[result_slot] = steps_to_goal;
  return NULL;
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

  unsigned int number;
  unsigned int testcases;

  pthread_t workers[100];
  solver_result inputs[100];

  infile >> testcases;
  DEBUG("number of test cases is " << testcases);
  for (int test=1; test <= testcases; test++) {
    infile >> number;
    inputs[test].number = number;
    inputs[test].result_slot = test - 1;
    pthread_create(&workers[test], NULL, solve_it, &inputs[test]);
  }
  for (int test=1; test <= testcases; test++) {
    pthread_join(workers[test], NULL);
  }
  output_results(testcases);

  infile.close();
  return 0;
}
