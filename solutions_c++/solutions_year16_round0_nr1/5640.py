#include <iostream>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int x=1; x<=T; x++) {
    long long N;
    cin >> N;

    if (N==0)
      cout << "Case #" << x << ": INSOMNIA" << endl;
    else {
      int i=0, missing=10; 
      bool digit[10];
      for (int j=0; j<10; j++) digit[j] = false;
      while (missing) {
	++i;
	for (long long y=N*i; y>0; y/=10){
	  int d=y % 10;
	  if (digit[d]==false) digit[d]=true, missing--;
	};
      };
      cout << "Case #" << x << ": " << N*i << endl;
    };
  };
};
