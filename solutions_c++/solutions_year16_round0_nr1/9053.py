// Counting sheep Google Code Jam 2016

#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

bool allDigits(const vector<int>& v) {
  for (int i : v) {
    if (i == 0) return false;
  }
  return true;
}

void doit(const long cs, const long num) {
  vector<int> digits(10, 0);
  if (num == 0) {
    cout << "Case #" << cs << ": INSOMNIA\n";
  } else {
    set<int> numbers;
    long n = num;
    long prev = num;
    while (!allDigits(digits) && numbers.find(n) == numbers.end()) {
      numbers.insert(n);
      while (n != 0) {
	int digit = n % 10;
	digits[digit] = 1;
	n = n / 10;
      }
      n = prev + num;
      prev = n;
    }
    if (allDigits(digits)) {
      cout << "Case #" << cs << ": " << prev - num<< "\n";
    } else {
      cout << "Case #" << cs << ": INSOMNIA\n";
    }
  }

  
}

void run() {
  string input;
  getline(cin, input);
  long count = atoi(input.c_str());
  for (long i = 0; i < count; ++i) {
    getline(cin, input);
    long num = atoi(input.c_str());
    doit(i+1, num);
  }
}

int main(int argc, const char* argv[]) {
  run();
}

  
