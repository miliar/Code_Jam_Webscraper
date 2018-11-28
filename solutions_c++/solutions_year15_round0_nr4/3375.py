#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int tc = 1 ; tc <= T ; tc++){    
    int X, R, C;
    
    cin >> X >> R >> C;
    
    bool ans = true;
    
    if(X > R && X > C) ans = false;
    else if(R * C % X != 0) ans = false;
    else if((X + 1) / 2 > min(R, C)) ans = false;
    else if(X == 4) ans = min(R, C) > 2;
    
    printf("Case #%d: ", tc);
    cout << (ans ? "GABRIEL" : "RICHARD") << endl;
    
  }
  return 0;
}
