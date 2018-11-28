#include <iostream>

using namespace std;

bool solveCase(int n){
    int S_max, i, k, stood = 0, added = 0;
    char c;
    cin >> S_max;

    for(stood = 0, i = 0; i < S_max + 1; i++){
        cin >> c;
        k = c - '0';
        if (stood < i){
            added += i - stood;
            stood += i - stood;
        }
        stood += k;
    }

    cout << "Case #" << n << ": ";
    cout << added << endl;
    return true;
}

int main(int argc, char** argv){
  int T;
  cin >> T;
  for(int i=0; i<T; i++){
    solveCase(i+1);
  }
  return 0;
}
