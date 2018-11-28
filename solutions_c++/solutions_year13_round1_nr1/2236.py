#include <cstdio>
#include <iostream>
using namespace std;

main() {
  int T,prob=1;
	long double r,t; 
	long y=0;
  for (cin >> T; T--;) {
    cin >> r >> t;
		y=0;
		do {
			y++;
			t-=2*r+1;
			r+=2;
			//cout << t <<endl;
		} while (t>=0.0);
    printf("Case #%d: %lu\n", prob++, y-1);
  }
}

