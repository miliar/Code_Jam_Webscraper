#include <iostream>
#include <string>

using namespace std;

int main () {
   int case_num;
   string input;
   cin >> case_num;
   for(int i = 1; i < case_num + 1; i++) {
      int num;
      int p[10] = {};
      int cnt = 0;
      int final_num = 0;
      cin >> num;
      if (num == 0) {
         cout << "Case #" << i << ": INSOMNIA" << endl;
         continue;
      }
      while(cnt != 10) {
         final_num += num; 
         int tmp = final_num;
         while(tmp) {
            int digit = tmp % 10;
            if (p[digit] == 0) {
               p[digit] = 1;
               cnt++;
            }
            tmp /= 10;
         }
      }
      cout << "Case #" << i << ": " << final_num << endl;
   }
   return 0;
}
