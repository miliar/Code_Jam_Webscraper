// emrecpp - Problem A

#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <cassert>

using namespace std;

string counting_sheep(const string &entry){
  bitset<10> digits(0);
  long N = stol(entry);
  if (N == 0) return "INSOMNIA";
  int m = 0;
  do {
    ++m;
    string mul_digits = to_string(m * abs(N));
    for(char d: mul_digits){
      digits[d - '0'] = 1;
    }
  } while (!digits.all());

  return to_string(m * N);
}

int main(void){
  int num_entries;
  cin >> num_entries; 
  for (int count = 1; count <= num_entries; ++count){
    string entry;
    cin >> entry;
    cout << "Case #" << count << ": " << counting_sheep(entry) << endl;
  }

  return 0;
}

