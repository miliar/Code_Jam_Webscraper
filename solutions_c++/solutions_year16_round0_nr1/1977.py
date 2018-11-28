#include <iostream>
#include <set>
#include <climits>
#include <stdlib.h>
#include <random>
#include <time.h>
#include <fstream>

using namespace std;

void process_case() {
  unsigned long long N;
  cin >> N;

  if (N == 0) {
    cout << "INSOMNIA";
    return;
  }

  set<unsigned long long> digits;
  for (unsigned long long i = 1; i < ULLONG_MAX / N; ++i) {
    auto current = i * N;
    if (current == 0) {
      digits.insert(0ULL);
      continue;
    }

    while (current > 0) {
      auto digit = current % 10;
      digits.insert(digit);
      current /= 10;
    }

    if (digits.size() == 10) {
      cout << i * N;
      return;
    }
  }
}

int main() {
  std::ifstream in("A-large.in");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("A-large.out");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!


  int T;
  cin >> T;

  for (int n = 0; n < T; ++n) {
    cout << "Case #" << (n + 1) << ": ";
    process_case();
    cout << endl;
  }
}

//int main() {
//  srand((unsigned)time(NULL));
//  cout << 100 << endl;
//  for (int i = 0; i < 100; ++i) {
//    int n = rand();
//    cout << n << endl;
//  }
//}