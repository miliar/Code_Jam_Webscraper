#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool isPalindrome(long long n) {
  char str[16];
  int nd = sprintf(str, "%I64d", n);

  int i = 0;
  int j = nd - 1;

  do {

    if (str[i] != str[j])
      return false;

    ++i;
    --j;

  } while (j > i);

  return true;
}

int main(int argc, char** argv) {

  srand(time(NULL));

  ifstream I((argc == 1) ? ("sample_input.txt") : (argv[1]));
  ofstream O("output.txt");
  string line;

  // pre-calc
  vector<long long> all;
  for (long long n = 1; n < 1e7; ++n) {
    if (isPalindrome(n)) {
      long long n2 = n*n;
      if (isPalindrome(n2))
        all.push_back(n2);
    }
  }

  int T; I >> T;

  for (int t = 0; t < T; ++t) {

    long long A, B; I >> A >> B;

    int count = 0;
    for (size_t i = 0; i < all.size() ; ++i) {

      if (A <= all[i] && all[i] <= B)
        ++count;
    }

    O << "Case #" << (t + 1) << ": " << count << endl;
  }

  I.close();
  O.close();

  return 0;
}
