#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

template<typename T>
void doReverse(T from, T to) {
  std::reverse(from, to);
  for (auto pos = from; pos != to; ++pos) {
    *pos = *pos == '-' ? '+' : '-';
  }
}

int main()
{
  int cases;
  cin >> cases;

  for (auto curCase = 1; curCase <= cases; curCase++) {

    string stack;
    cin >> stack;
    int result = 0;

    auto alignedTop = stack.end();
    while (alignedTop != stack.begin()) {
      if (*(alignedTop - 1) == '+') {
        --alignedTop;
      }
      else if (*stack.begin() == '-') {
        doReverse(stack.begin(), alignedTop);
        ++result;
      }
      else if (*stack.begin() == '+') {
        auto pos = stack.begin();
        while (*pos == '+') {
          ++pos;
        }
        doReverse(stack.begin(), pos);
        ++result;
      }
    }

    cout << "Case #" << curCase << ": " << result << endl;
  }
}

