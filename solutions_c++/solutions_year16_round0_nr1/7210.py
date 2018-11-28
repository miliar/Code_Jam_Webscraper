
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

map<char, bool> m = {{'1', false}, {'2', false}, {'3', false}, {'4', false},
                    {'5', false}, {'6', false}, {'7', false}, {'8', false},
                    {'9', false}, {'0', false}};

bool checkdone() {
  for(auto &kv : m) {
    if(kv.second == false)
      return false;
  }
  return true;
}


int main() {
  int kases;
  cin >> kases;

  for(int k = 0; k < kases; k++){
    long N;
    cin >> N;
    
    if(N == 0) {
      cout << "Case #" << k+1 << ": INSOMNIA" << endl;
      continue;
    }

    long i = 1;
    while(!checkdone()) {
      char a[10000];
      sprintf(a, "%d", N * i);

      for(int q = 0; q < strlen(a); q++) {
        char c = a[q];
        m[c] = true;
      }
      i++;
    }

    cout << "Case #" << k+1 << ": " << N*(i-1) << endl;
    m = {{'1', false}, {'2', false}, {'3', false}, {'4', false},
                        {'5', false}, {'6', false}, {'7', false}, {'8', false},
                        {'9', false}, {'0', false}};

  }
  return 0;
}
