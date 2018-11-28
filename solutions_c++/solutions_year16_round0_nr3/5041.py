// coinjam Google Code Jam 2016

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <math.h>

using namespace std;

const int NUM = 16;

//typedef vector<unsigned char> Bitfield;

typedef unsigned long long ull;

string printIt(const bitset<NUM> & bits) {
  int len = bits.size();
  string s = "";
  for (int i = 0; i < len; ++i) {
    s += ((bits[len - 1 - i] == 0) ? "0" : "1");
  }
  return s;
}

ull getNumInBase(const bitset<NUM> & bit, int base) {
  ull num = 0;
  for (int i = bit.size() - 1; i >= 0; --i) {
    num *= base;
    bool b = bit[i];
    if (b) {
      num += 1;
    }
  }
  return num;
}

ull checkPrime(const ull & num) {
  ull d = sqrtl(num);
  for (ull i = 2; i < d; ++ i) {
    if (num % i == 0) {
      return i;
    }
  }
  return 0;
}

int doIt(const bitset<NUM> & bits) {
  vector<ull> divisors;
  for (int i = 2; i < 11; ++i) {
    ull num = getNumInBase(bits, i);
    ull p = checkPrime(num);
    if (p != 0) {
      divisors.push_back(p);
    } else {
      return 0;
    }
    //    string s = printIt(bits);
    // cout << s << " in base " << i << " is " << num << "\n";
  }
  string s = printIt(bits);
  cout << s;
  for (ull d : divisors) {
    cout << " " << d;
  }
  cout << endl;
  // get num in base
  // sqrt
  // is it prime?
  // if not continue
  return 1;
}

void genAll(int len, int num) {
  int middle = len - 2; // number of middle digits
  int total = 1; // bit combinations of middle (3 bits -> 8 bit patterns)
  // total
  for (int i = 0; i < middle; ++i) {
    total *= 2;
  }
  //  cout << "total " << total << "\n";
  int count = 0;
  for (int i = 0; i < total; ++i) {
    bitset<NUM> bits;
    bits.reset(); // to 0
    bits[len -1] = bits[0] = 1;
    // get bit pattern, fill out bits
    for (int j = 0; j < middle; ++j) {
      bits[1 + j] = (i & (1 << j));
    }
    count += doIt(bits);
    if (count >= num) {
      break;
    }
    //printIt(bits);
  }


}

void run() {
  string input;
  getline(cin, input);
  cout << "Case #1:\n";
  int len, num;
  cin >> len >> num;
  // cout << len << " " << num << "\n";
  genAll(len, num);
}

int main(int argc, const char* argv[]) {
  run();
}

  
