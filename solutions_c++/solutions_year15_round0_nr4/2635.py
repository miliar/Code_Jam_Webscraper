#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cctype>
using namespace std;

int main(){
 int Case(0);
 int N;
 cin >> N;
 for (; Case < N; ++Case){
  int x, r, c;
  cin >> x >> r >> c;
  string ans;
  switch (x){
   case 1:		// One Omino
    ans = "GABRIEL";
    break;
   case 2:		// Two Omino
    if (r%2 && c%2){	// if an odd number of squares
     ans = "RICHARD";
    } else {
     ans = "GABRIEL";
    }
    break;
   case 3: // Size 3 omino
    if (r*c%3){
     ans = "RICHARD";
    } else if (r*c == 3){
     ans = "RICHARD";
    } else {
     ans = "GABRIEL";
    }
    break;
   case 4:
    if (r*c%4){
     ans = "RICHARD";
    } else if (r*c == 4 || r*c == 8){
     ans = "RICHARD";
    } else {
     ans = "GABRIEL";
    }
  }

  cout << "Case #" << Case+1 << ": " << ans << endl;
 }
 return 0;
}
