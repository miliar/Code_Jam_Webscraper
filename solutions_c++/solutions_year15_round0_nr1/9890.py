#include <iostream>
using namespace std;

int main() {
   char audience[1001];
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++) {
      int friends = 0;
      int len;
      cin >> len;
      cin.get();
      cin.getline(audience, len+2);
      for (int j = 0, standing = 0; j <= len; j++) {
         char &tmp = audience[j];
         tmp -= '0';
         if (tmp && standing < j) {
            int diff = j - standing;
            friends  += diff;
            standing += diff;
         }
         standing += tmp;
      }
      cout << "Case #" << i << ": " << friends << endl;
   }
   return 0;
}
