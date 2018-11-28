#include <iostream>
#include <string>

using namespace std;

int
main() {
  int T; 

  cin >> T;

  for(int c = 1; c <=T; c++) {
    int N;
    string s;

    cin >> N; 
    cin >> s;

    int up = 0;
    int n = 0;
    for(int i = 0; i < s.length(); i++) {
      int S = s[i]-'0';

      if(up < i) {
	n += i - up;
	up = i;
      }
      up += S;
    }

    cout << "Case #" << c << ": " << n << endl;
  }

  return 0;
}

