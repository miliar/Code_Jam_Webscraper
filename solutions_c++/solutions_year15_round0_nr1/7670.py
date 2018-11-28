#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int cases,shylvls;
  cin >> cases;
  for (int casenum = 1; casenum <= cases; casenum ++) { 
    string audmems;
    int friends = 0,standing = 0;
    cin >> shylvls >> audmems;
    for (int i = 0; i <= shylvls; i++) {
      if (standing < i) {
        friends += (i-standing);
	standing = i;
      }
      standing += audmems[i]-'0';
    }
    cout << "Case #" << casenum << ": " << friends << endl;
  }

  return 0;
}
