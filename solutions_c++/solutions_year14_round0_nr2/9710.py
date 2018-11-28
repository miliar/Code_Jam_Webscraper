#include <iostream>
#include <iomanip> 
using namespace std;
typedef long double dd;
int T;
dd C, F, X;
dd f(int x) {
  dd a=0;
  for (int i=0; i<x; i++) {
    a += dd(C)/dd(F*i+2);
  }
  a += X/(F*x+2);
  return a;
}

int ternarySearch(int l, int r) { //copied this from wikipedia, too tired to code; :P
  if (r-l<=2) return l;
  int leftThird = (2*l + r)/3;
  int rightThird = (l + 2*r)/3; 
  if (f(leftThird) > f(rightThird))
    return ternarySearch(leftThird, r);
  else
    return ternarySearch(l, rightThird);
}
int main() {
  cin >> T;
  for (int asd=1; asd<=T; asd++) {
    cout.precision(7);
    cout << fixed;
    cin >> C >> F >> X;
    int k;
    //k = ternarySearch(0, X/2+1);
    dd ans = 6999999999;
    for (k=0; k<X; k++) {
      ans = min(ans, f(k));
    }
    cout <<  "Case #" << asd << ": "  << ans << endl;
  }
  return 0;
}
