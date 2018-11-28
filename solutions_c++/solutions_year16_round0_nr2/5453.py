#include <iostream>
#include <vector>

int flip(std::string pc) {
  std::vector<bool> pcs;
  std::string::iterator itr = pc.begin();
  bool curr_state = true;
  int total_flips = 0;

  while(itr != pc.end()) {
    if(*itr == '+') {
      pcs.push_back(true);
    } else {
      pcs.push_back(false);
    }
    ++itr;
  }

  std::vector<bool>::reverse_iterator itr2 = pcs.rbegin();
  while(itr2 != pcs.rend()) {
    if(curr_state != *itr2) {
      curr_state = !curr_state;
      ++total_flips;
    }
    ++itr2;
  }
  return total_flips; 
}


int main() {
  int counter = 1;
  int cases = 0;
  std::cin >> cases;
  while(cases--) {
    std::string pancakes;
    std::cin >> pancakes;
    int res = flip(pancakes);
    std::cout << "Case #" << counter << ": ";
    std::cout << res << "\n";
    ++counter;
  }
  return 0;
}
