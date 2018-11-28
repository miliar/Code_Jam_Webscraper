#include <iostream>
#include <string>

using namespace std;

main () { 
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int Smax,sum=0,friends=0;
    string S;
    cin >> Smax >> S;
    //    cout << "*" << S << "*" << endl;
    
    for (int i=0; i<=Smax; i++) {
      //      cout << S[i] << "." ;
      if (S[i] != '0')
	friends = max(friends, i-sum);
            sum += S[i] - '0';
    };
    //    cout << "sum=" << sum << endl;
    cout << "Case #" << t << ": " << friends << endl;
  };
};
