#include <iostream>
#include <stack>
#include <string>

using namespace std;

void transform(int index, string& cakes);
bool done(const string &cakes);

int main() {
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    string input;
    cin >> input;
    int count = 0;
    while(!done(input)) {
      bool got_minus = false;
      size_t first_minus = input.find_first_of('-');
      size_t j;
      for(j = first_minus; j < input.size() && input[j] == '-';j++);

      if(first_minus != 0) {
        transform(first_minus, input);
        count++;
      }
      transform(j, input);
      count++;
    }
    cout << "Case #" << i << ": " << count << endl;
  }
}

bool done(const string &cakes) {
  for(int i = 0; i < cakes.size(); i++) {
    if(cakes[i] == '-') return false;
  }

  return true;
}

void transform(int index, string& cakes) {
  string store;
  for(int i = index - 1, j = 0; j < index; j++, i--) {
    store[j] = cakes[i] == '-' ? '+' : '-';
  }
  for(int i = 0; i < index; i++) cakes[i] = store[i];
}
