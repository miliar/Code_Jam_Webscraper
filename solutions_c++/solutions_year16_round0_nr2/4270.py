#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int main() {
   int T, len;
   cin >> T;
   for (int t = 1; t <= T; ++t) {
      string S, X;
      cin >> S;
      int c = 0;
      for (int i = 0, len = S.length(); i < len; ++i) X += '+';
      for (int i = S.length() - 1; i >= 0; --i) {
         if (S[i] != X[i]) {
            //cout << S << "[" << i << "]: " << X << " => ";
            for (int j = 0, len = i + 1; j < len - j; ++j) {
               char t = X[j];
               X[j] = X[len - j - 1] == '-' ? '+' : '-';
               X[len - j - 1] = t == '-' ? '+' : '-';
            }
            //cout << X << endl;
            ++c;
         }
      }
      cout << "Case #" << t << ": " << c << endl;
   }
   return 0;
}