#include<iostream>
#include <string>
#include <set>
using namespace std;

void pass(int currCase, int result) {
  cout << "Case #" <<currCase <<": "<<result<< endl;      
}

int main () {
  int cases, currCase = 0, i, j;
  unsigned int a, b, k, count;
  cin >> cases;
  while (currCase++ < cases) {
    count = 0;
    cin >> a >> b >> k;
    for ( i = 0; i < a; i++ ) {
      for ( j = 0; j < b; j++ ) {
        if ( (i&j) < k ) count++;
      }
    }
    pass(currCase, count);
  }
  return 0;
}
