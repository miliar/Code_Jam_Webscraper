#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <fstream>
#include <string>
using namespace std;

std::vector<unsigned int> input_values;
std::vector<unsigned int> max_set;

void populate_max_set() {
  max_set.clear();
  for (unsigned int i = 0; i < 10; i++) {
    max_set.push_back(i);
  }
}

bool is_max_set_empty() {
  return (max_set.size() == 0);
}

void remove_from_max_set(const unsigned int num) {
  max_set.erase(std::remove(max_set.begin(), max_set.end(), num), max_set.end());
}

void SplitNumber(unsigned int number, std::set<int>* digits) {
  if (number == 0) {
    digits->insert(0);
  } else {
    while (number != 0) {
      unsigned int last = number % 10;
      digits->insert(last);
      number = (number - last) / 10;
    }
  }
}

void print(const unsigned int n, const unsigned int input_val) {
  cout << n << ": " << input_val << endl;

  cout << "MAX SET " << endl;
  for (auto const it : max_set) {
    cout << it << endl;
  }
}

int64_t DetermineSleep(const unsigned int input_val, const unsigned int n) {
  std::set<int> digits;
  SplitNumber(input_val * n, &digits);

  for (auto it : digits) {
    remove_from_max_set(it);
  }

  //print(n , input_val);

  int64_t ret_val = 0;
  if (is_max_set_empty()) {
    ret_val = input_val * n;
  } else {
    ret_val = DetermineSleep(input_val, n+1);
  }
  return ret_val;
}

int main(int argc, char* argv[])
{

   ifstream myfile ("input.txt");
    if (myfile.is_open())
    {
      std::string line;
      while ( getline (myfile,line) )
      {
        input_values.push_back(atoi(line.c_str()));
      }
      myfile.close();
    }

    unsigned int num_test_cases = input_values.size();

    ofstream out ("output.txt");
    if (out.is_open()) {
      for (unsigned int i = 0; i < num_test_cases; i++) {
        populate_max_set();
        if (input_values[i] == 0) {
          out << "Case #" << i+1 << ": INSOMNIA" << endl;
        } else {
          out << "Case #" << i+1 << ": " << DetermineSleep(input_values[i], 1) << endl;
        }
      }
    }
    out.close();
    return 0;
}
