#include <iostream>
#include <limits>
#include <bitset>

using namespace std;

typedef bitset<100> Stack;

Stack makeStack(const std::string& line) {
  Stack res;
  res.set();
  for (size_t i = 0; i < line.size(); ++i) {
    if (line[i] == '-') {
      res.reset(i);
    }
  }
  return res;
}

size_t getBack(const Stack& stack, size_t start) {
  for (size_t i = start; i ; --i) {
    if (!stack.test(i-1)) {
      return i;
    }
  }
  return 0;
}

unsigned long long solve(Stack& stack, unsigned long long count, size_t start) {
  auto back = getBack(stack, start);
  if (0 == back) {
    return count;
  }

  bool flippedTop = false;
  // First flip the positives on the top
  size_t topPos; 
  for (topPos = 1; topPos <= back; ++topPos) {
    if (!stack.test(topPos-1)) {
      stack.flip(topPos-1);
      flippedTop=true;
    } else {
      break;
    }
  }
  count = (flippedTop) ? count + 1 : count;
  if (topPos > back) {
    topPos = back;
  }

  if (topPos != back) {
    for (size_t i = 0; i < back; ++i) {
      stack.flip(i);
    }
    return solve(stack, count+1, back);
  } else {
    return count;
  }
}

int main() {
  std::ios::sync_with_stdio(false);

  int T; cin >> T;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  for (int i = 1; i <= T; ++i) {
    std::string line;
    getline(cin, line);
    Stack stack = makeStack(line);
    cout << "Case #" << i << ": " << solve(stack, 0, stack.size()) << "\n";
  }

}
