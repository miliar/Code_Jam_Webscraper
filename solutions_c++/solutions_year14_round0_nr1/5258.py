#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";
    int r1, r2;
    cin >> r1;
    int cand[4];
    for (int j = 1; j <= 4; ++j) {
      for (int k = 0; k < 4; ++k) {
	int a;
	cin >> a;
	if (j == r1) {
	  cand[k] = a;
	}
      }
    }
    cin >> r2;
    int hit = 0;
    int ans = 0;
    for (int j = 1; j <= 4; ++j) {
      for (int k = 0; k < 4; ++k) {
	int a;
	cin >> a;
	if (j == r2) {
	  for (int p = 0; p < 4; ++p) {
	    if (a == cand[p]) {
	      ++hit;
	      ans = a;
	    }
	  }
	}
      }
    }
    if (hit == 0) {
      cout << "Volunteer cheated!" << endl;
    } else if (hit == 1) {
      cout << ans << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
}
    
