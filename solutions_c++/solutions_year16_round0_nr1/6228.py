#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;

bool has_all(int digit[]) {
  for (int i = 0; i < 10; ++i) {
   	if (digit[i] == 0) {
      return false;
    }
  }
  return true;
}

void extract(uint64_t n, int digit[]) {
  while (n) {
    digit[n % 10]++;
    n /= 10;
  }
}

uint64_t go(uint64_t n) {
  int digit[10] = {0};
  uint64_t m = n;
  int i = 1;
  while (!has_all(digit)) {
    m = (n * i);
  	extract(m, digit);
    i++;
  }
  return m;
}

void inout_counting_sheep(istream &in, ostream &out) {
 	int t; 
  in >> t;  
  uint64_t n;
  for (int c = 1; c <= t; ++c) {
    in >> n;
    out << "Case #" << c << ": ";
    if (n == 0) {
      out << "INSOMNIA";
    } else {
      out << go(n);
    }
    out << endl;
  }
}

int main() {
  ifstream in("in.txt");
  ofstream out("out.txt");
  inout_counting_sheep(in, out);
  return 0;
}



