#include <iostream>
#include <stdio.h>


using namespace std;



void cs(int c) {
  int l;
  cin >> l;

  //  cout << "l: " << l << endl;

  int s = 0;
  int e = 0;

  getchar();

  //last is not relevant
  for (int i = 0; i < l; i++) {
    int n;
    n = getchar();
    int nn = n - '0';
    //    cout << "n: " << nn << endl;
    s += nn;

    if ( i >= s) {
      s++;
      e++;
    }
  }
 
  getchar();
  //  cout << "cc:" << cc << endl;
  cout << "Case #" << c << ": " << e << endl;
}

int main() {
  int cases;
  cin >> cases;

  for (int i = 0; i < cases; i++) {
     cs(i+1);
  }
}
