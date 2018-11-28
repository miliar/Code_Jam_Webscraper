#include <iostream>
#include <string>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int x=1; x<=T; x++) {
    string S;
    cin >> S;
    int flips=0, i=S.length()-1;
    while (i>=0 && S[i]=='+') i--;
    while (i>=0) {
      while (i>=0 && S[i]!='+') i--;
      flips ++;
      if (i>=0) {
	while (i>=0 && S[i]=='+') i--;
	flips ++;
      };
    };
    cout << "Case #" << x << ": " << flips << endl;
  };
};

