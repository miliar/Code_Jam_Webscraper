// g++ -lm -lcrypt -O2 -std=c++11 -pipe main.cpp && ./a.out

#include <bitset>
#include <iostream>
#include <fstream>
bool verbose;

void checkDigits(std::bitset<10>& hist, long long n) {
  while(n>0) {
    hist[n%10] = true;
    n /= 10;
  }
}

void display(std::bitset<10>& hist) {
  if (!verbose) return;
  std::cout << "|";
  for (int i = 9; i >= 0; i--) {
    std::cout << (hist[i] ? "*" : " ");
  }
  std::cout << "|"<<std::endl;

}

int count(long long N) {
  if (verbose)
    std::cout << "+----------+" << std::endl;
  std::bitset<10> hist;
  hist.reset();
  int i;
  for (i = 1; i < 120000; i++) {
    checkDigits(hist, N*i);
    display(hist);
    if (hist.none()) return -1;
    if (hist.all()) break;
  }
  if (verbose)
    std::cout << "+----------+" << std::endl;
  return i;
}

void testNum(int n) {
  std::cout << n << ": " << count(n) << std::endl;
}

void testHist(int n) {
  std::bitset<10> hist;
  hist.reset();
  display(hist);
  checkDigits(hist, 1);
  display(hist);
}

int main(int argc, char *argv[]) {
  if (argc == 2) {
    verbose = false;
    std::ifstream ifs(argv[1]);
    int cnt;
    ifs >> cnt;
    for(int i = 0; i < cnt; i++) {
      int n;
      ifs >> n;
      auto c = count(n);
      std::cout << "Case #" << (i+1) << ": ";
      if (c >= 1 )
	std::cout << c * n;
      else 	
	std::cout << "INSOMNIA";
      std::cout << std::endl;
    }
  } else {
    // testHist(42);
    // testNum(1234567890);
    // testNum(1337);
    // testNum(1692);
    // for (int i = 0; i < 1337; i++) {
    //   testNum(i);
    // }
    testNum(3ul);
  }
  return 0;
}
