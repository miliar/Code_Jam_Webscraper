#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#define INF 2147483647
using namespace std;

int main(int argc, const char * argv[]) {

  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int cases, currCase = 0, a, b, r1[4], r2[4], g, selectedNumber, numberCount = 0;
  cin >> cases;
  while(currCase++ < cases) {
    cin >> a;
    for(int i = 0; i < 4; i++ ) {
      if ( i == a-1 ) {
        cin >> r1[0] >> r1[1] >> r1[2] >> r1[3];
      } else {
        cin >> g >> g >> g >> g;
      }
    }
    cin >> b;
    for(int i = 0; i < 4; i++ ) {
      if ( i == b-1 ) {
        cin >> r2[0] >> r2[1] >> r2[2] >> r2[3];
      } else {
        cin >> g >> g >> g >> g;
      }
    }
    numberCount = 0;
    for ( int i = 0; i < 4; i++) {
      for ( int j = 0; j < 4; j++) {
        if ( r1[i] == r2[j] ) {
          numberCount++;
          selectedNumber = r1[i];
        }
      }
    }
    if ( 1 == numberCount ) {
      cout << "Case #" <<currCase <<": "<<selectedNumber << endl;
    } else if ( 0 == numberCount ) {
      cout << "Case #" <<currCase <<": Volunteer cheated!" << endl;
    } else {
      cout << "Case #" <<currCase <<": Bad magician!" << endl;      
    }
  }
  return 0;
}
