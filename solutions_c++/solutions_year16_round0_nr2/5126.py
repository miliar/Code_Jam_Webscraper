#include<iostream>
#include<string>
using namespace std;

int main() {
   int T, x, y, i;
   char last;
   string S;
   cin >> T;
   for (x = 1; x <= T; x++) {
      cin >> S;
      last = 'a';
      y = 0;
      for (i = 0; i < S.length(); i++) {
         if (S[i] != last) {
            y++;
            last = S[i];
         }
      }
      y = S[i-1] == '+' ? y-1 : y;
      cout << "Case #" << x << ": " << y << endl;
   }
   return 0;
}
