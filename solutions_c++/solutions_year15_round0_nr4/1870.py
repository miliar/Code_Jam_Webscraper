#include<iostream>

using namespace std;


int main() {
  unsigned int T;

  cin >> T;

  for (unsigned int t=1; t<=T; ++t) {
    string y="RICHARD";
    unsigned int X, R, C;
    cin >> X >> R >> C;
    if (((R*C)%X)==0) {
      switch (X) {
      case 1:
      case 2:
	y="GABRIEL"; break;
      case 3:
	if (R>1&&C>1) y="GABRIEL";
	break;
      case 4:
	if ((R>=3&&C>=4)||(R>=4&&C>=3)) y="GABRIEL";
	break;
      }
    }
    cout << "Case #" << t << ": " << y << endl;
  }
  return 0;
}
