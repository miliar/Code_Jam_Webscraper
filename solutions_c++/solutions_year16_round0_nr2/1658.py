#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void flip(std::string &stack, uint32_t pos) {
  char c = stack[pos];

  for(pos = pos+1; pos < stack.size(); ++pos) {
    if(stack[pos] != c)
      break;
  }

  pos -= 1;

  for(uint32_t i = 0; i <= pos; ++i) {
    if(stack[i] == '-')
      stack[i] = '+';
    else
      stack[i] = '-';
  }
}

uint32_t solve(std::string pancakes) {
  uint32_t moves = 0;
  char last = '+';

  //cout << "0: " << pancakes << endl;

  for(uint32_t i = 0; i < pancakes.size(); ++i) {
    if(pancakes[i] != last) {
      flip(pancakes, i);
      ++moves;
      //cout << moves << ": " << pancakes << endl;

      if(pancakes[0] == '-') {
        i = -1;
        last = '+';
      }
    }
    else
      last = pancakes[i];
  }

  return moves;
}

int main() {
  uint32_t cases;
  std::string stack;

  cin >> cases;

  for(uint32_t i = 0; i < cases; ++i) {
    cin >> stack;

    cout << "Case #" << i+1 << ": " << solve(stack) << std::endl;
  }

  return 0;
}
