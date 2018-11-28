#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;

std::string flip_stack(std::string stack, int index);
int first_minus_from_bot(std::string s);
int first_minus_from_top(std::string s);

int main() {
  string input;
  cin >> input;
  int cases = atoi(input.c_str());
  std::string stack;
  int top=0, bot=0;
  for (int i = 1; i <= cases; i++) {
    cin >> stack;
    cout << "Case #" << i << ": ";
    int j = 0;
    while ((top = first_minus_from_top(stack)) != -1) {
      // first: first minus from the top
      if (top > 0) {
        stack = flip_stack(stack, top-1);
        j++;
      }
      if ((bot = first_minus_from_bot(stack)) != -1) {
          stack = flip_stack(stack, bot);
          j++;
      }
      else {
        break;
      }
    }
    cout << j << endl;
  }
}

int first_minus_from_top(std::string s) {
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '-')
      return i;
  }
  return -1;
}

int first_minus_from_bot(std::string s) {
  for (int i = s.size()-1; i >= 0; i--) {
    if (s[i] == '-')
      return i;
  }
  return -1;
}

std::string flip_stack(std::string stack, int index) {
  std::string flip = stack;
  char op = '\0';
  for (int i = 0; i <= index; i++) {
    op = stack[i];
    op = (op=='-')?'+':((op=='+')?'-':op);
    flip[index-i] = op;
  }
  return flip;
}
