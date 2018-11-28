#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  string S;
  for(int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";
    long long flips = 0;
    cin >> S;
    bool top = (S[0] == '+');
    bool turn = false;
    for(int j = 0; j < S.size(); ++j) {
      if(S[j] == '-') {
	turn = true;
	continue;
      }
      if(turn) {
	turn = false;
	if(top) {
	  flips += 2;
	} else {
	
	  flips++;
	  top = true;
	}
      }
    }
    if(S[S.size()-1] == '-')
      flips += top ? 2 : 1;
    cout << flips << endl;
  }
}
