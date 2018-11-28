#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

bool digits[10] = {false};

void reset() {
  for(int i = 0; i < 10; ++i) digits[i] = false;
}

void flagDigits(long long nr) {
  while(nr > 0) {
    digits[nr%10] = true;
    nr = nr / 10;
  }
}

int main() {
  int nrTasks;
  cin >> nrTasks;
  for(int i = 1; i <= nrTasks; ++i) {
    reset();
    long long n;
    cin >> n;
    long long nr = n;
    bool found = false;
    cout << "Case #" << i << ": ";
    for(int j = 0; !found && j < 100000; ++j) {
      flagDigits(nr);
      bool finished = true;
      for(int h = 0; finished && h < 10; ++h) {
        finished = digits[h];
      }
      if(finished) {
        cout << nr << endl;
        found = true;
      }
      nr += n;
    }
    if(!found) {
      cout << "INSOMNIA" << endl;
    }
  }
  return 0;
}