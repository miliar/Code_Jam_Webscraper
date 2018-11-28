#include <iostream>
using namespace std;
typedef long long LL;

//*******************
//*******************

int main() {
   ios::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int i = 1; i <= T; ++i) {
      int max_lvl;
      string s;
      cin >> max_lvl >> s;
      int result = 0;
      int count_standing = 0;
      for(int j = 0; j < s.size(); ++j) {
         int people = s[j] - '0';
         if(count_standing < j) {
            result += j -  count_standing;
            count_standing = j + people;
         }
         else
            count_standing += people;
      }
      cout << "Case #" << i << ": " << result << endl;
   }
   return 0;
}