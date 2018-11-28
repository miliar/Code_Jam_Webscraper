#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <=T; t++) {
    int M; string S;
    cin >> M >> S;
    int n = 0; int v = 0;
    for(int i = 0; i <= M; i++) { 
      if(n + v < i) v = i - n;
      n += S[i] - '0';
    }
    cout << "Case #" << t << ": " << v << endl;
  }
}
