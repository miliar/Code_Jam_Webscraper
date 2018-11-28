#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long LL;

//*******************
//*******************

int winner(int X, int w, int h) {
   // 1 <= X, h, w <= 4
   if(w * h % X != 0)
      return 0;
   if(X == 1 || X == 2)
      return 1;
   if(X == 3) {
      if(w == 1 || h == 1)
         return 0;
      else
         return 1;
   }
   if(X == 4) {
      if(w == 1 || w == 2)
         return 0;
      else
         return 1;
   }
   return 0;
}

string solve() {
   int X, w, h;
   cin >> X >> w >> h;
   if(winner(X, min(w, h), max(w, h)) == 0)
      return "RICHARD";
   return "GABRIEL";
}

int main() {
   ios::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int i = 1; i <= T; ++i)
      cout << "Case #" << i << ": " << solve() << endl;
   return 0;
}