#include <iostream>
#include <string>
#include <vector>

using namespace std;

void print(vector<char> &v) {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i];
  }

  cout << endl;
}

int get_start_pos(vector<char> &v) {
  for (int i = v.size() - 1; i >= 0; i--) {
    if (v[i] == '-')
      return i;
  }

  return -1;
}

inline char swap_char(char c) {
  if (c == '-')
    return '+';
  else
    return '-';
}

void swap_stack(vector<char> &v, int pos) {
  for (int i = 0; i <= pos / 2; i++) {
    char tmp = v[i];
    v[i] = swap_char(v[pos - i]);
    v[pos - i] = swap_char(tmp);
  }
}

void process_stack(vector<char> &v, int pos) {
  int pluscount = 0;
  while (v[pluscount] == '+')
    pluscount++;

  if (pluscount > 0) {
    swap_stack(v, pluscount - 1);
  } else {
    swap_stack(v, pos);
  }
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    string stack;
    cin >> stack;

    vector<char> v(stack.begin(), stack.end());

    int start_pos = get_start_pos(v); 
    int steps = 0;
    while (start_pos >= 0) {
      process_stack(v, start_pos); 
      start_pos = get_start_pos(v); 
      steps++;
    }

    cout << "Case #" << i + 1 << ": " << steps << endl;

     /*  
    --+-
    +-++
    --++
    ++++


    -++-
    +--+
    ---+
    ++++

    ---+
    ++++

    +---
    ----
    ++++

    ----+--++--+
    ++--++-+++++
    ----++-+++++
    +--+++++++++
    ---
    ++++++++++++
    */
  }

  return 0;
}
