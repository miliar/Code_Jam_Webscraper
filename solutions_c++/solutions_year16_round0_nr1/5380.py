#include <iostream>
#include <string>
#include <set>

void add_to_set(int curr_num, std::set<char>& found_digits) {
  std::string string_num = std::to_string(curr_num);
  std::string::iterator itr = string_num.begin();
  while(itr != string_num.end()) {
    found_digits.insert(*itr);
    ++itr;
  }
}

int do_count(int initial_num) {
  bool firstcase = true;
  int curr_num = initial_num;
  std::set<char> visited_digits;
  
  while(visited_digits.size() != 10) {
    if(firstcase) {
      firstcase = false;
    } else {
      curr_num += initial_num;
    }
    if(curr_num == 0) {
      return -1;
    }

    add_to_set(curr_num, visited_digits);
  }

  return curr_num;
}

int main() {
  int cases = 0;
  int counter = 1;
  std::cin >> cases;
  while(cases--) {
    int curr_num;
    std::cin >> curr_num;
    int res = do_count(curr_num);
    std::cout << "Case #" << counter << ": ";
    if(res == -1) {
      std::cout << "INSOMNIA" << "\n";
    } else {
      std::cout << res << "\n";
    }
    ++counter;
  }
  return 0;
}
