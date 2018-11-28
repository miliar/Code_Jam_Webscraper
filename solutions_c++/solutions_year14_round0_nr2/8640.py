#include <iostream>
#include <stdio.h>
#include <iomanip>

#define LD long double

using namespace std;

LD solve(LD c, LD f, LD x) {
  LD p = 2.0;
  LD ans = x / p, cur = 0;
  for(int i =  0; i < 1000000; i++) {
    cur += c / p; p += f;
    ans = min(ans, cur + x / p);   
    //cout << ans << ' ' << p << ' ' << cur << endl;
  }
  return ans;
}

int main() {
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);

  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    LD C, F, X;
    cin >> C >> F >> X;
    cout << "Case #" << t << ": ";
    cout << setprecision(7) << fixed << solve(C, F, X) << endl;
    //cout << "Impossible" << endl;
  } 

}