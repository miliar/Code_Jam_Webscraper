#include <iostream>
#include <sstream>

using namespace std;

int analyse(const string& stack) {
  bool current = true;
  int count = 0;
  for (int i = stack.size()-1; i >=0; --i) {
    bool hp = stack[i] == '+';
    if (hp != current) {
      ++count;
    }
    current = hp;
  }
  return count;
}

int main (int argc, char *argv[])
{
  string num;
  getline(cin, num);
  istringstream snum(num);
  int n = 0;
  snum >> n;
  for (int i = 0; i < n; ++i)
  {
    string stack;
    getline(cin, stack);
    cout << "Case #" << i+1 << ": " << analyse(stack) << endl;
  }
  return 0;
}

