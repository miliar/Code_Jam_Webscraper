#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <iterator>

using namespace std;

#define TWO(x) (x)*(x)
#define MAX(x,y) {if(x<(y)) x=(y);}
#define MIN(x,y) {if(x>(y)) x=(y);}
#define ALL(x) (x).begin(), (x).end()

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  double C, F, X, G;
  cin >> T;
  for(int i = 0; i < T; ++i) {
    cin >> C >> F >> X; 
    int n = X+1;
    double time = 0;
    double ans = X/2.0;
    for(int j = 0; j < n; ++ j) {
      time += C/(2+F*j);
      G = time + X/(2+F*(j+1));
      if(G < ans) ans = G;
    }
    cout << "Case #" << i + 1 << ": ";
    cout << setprecision(7) << fixed << ans << endl;
  }
  return 0;
}


