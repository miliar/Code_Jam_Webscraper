#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int A, B;

int in[4][4], fi[4][4];

int test() {
  cin >> A;
  for (int i=0; i<4; i++) 
	for (int j=0; j<4; j++) cin >> in[i][j];
  cin >> B;
  for (int i=0; i<4; i++) 
	for (int j=0; j<4; j++) cin >> fi[i][j];
  int c=0, a;
  for (int i=0; i<4 && c<2; i++) {
	for (int j=0; j<4; j++) {
	if (in[A-1][i]==fi[B-1][j]) {
	  c++;
	  a=in[A-1][i];
	}
	}
  }
 // cout <<  endl << "ans " << c << " " << a << endl;
  if (c==0) return -3;
  if (c==1) return a;
  if (c>1) return -1;
}

int main() {
  int T, r;
  cin >> T;
  ofstream fout("magic.out");
  for (int i=0; i<T; i++) {
	r=test();
	if (r==-3) {
	  fout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
	}
	else if (r==-1) {
	  fout << "Case #" << i+1 << ": Bad magician!" << endl;
	}
	else {
	  fout << "Case #" << i+1 << ": " << r << endl;
	}
  }
  return 0;
}


