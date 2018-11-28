#include <iostream>
#include <set>
using namespace std;

int main()
{
   int n;
   cin >> n;
   int casen = 1;
   while (n--) {
      int num;
      cin >> num;
      set<char> digits;
      int i;
      bool fall_asleep=false;
      string s;
      for (i=1; i<100000; ++i) {
         s = to_string(num * i);
         for (int j =0 ; j<s.size(); ++j) {
            digits.insert(s[j]);
            if (digits.size() == 10) {
                 fall_asleep = true;
                 break;
            }
         }
         if (fall_asleep) {
             break;
         }
      }
      cout << "Case #" << casen++ << ": " << (fall_asleep ? s : "INSOMNIA") << endl;
   }
   return 0;
}
