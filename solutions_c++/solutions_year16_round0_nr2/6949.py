#include <iostream>
#include <string>
using namespace std;

int main () {
   int case_num;
   string input;
   cin >> case_num;
   for(int i = 1; i < case_num + 1; i++) {
      int result = 0;
      char prev = ' ';
      cin >> input;
      if (input[0] == '-') {
         result = 1;
      } 
      
      for (int j = 0; j < input.length(); j++) {
         char cur = input[j];
         if (cur == '-' && prev == '+') {
            result += 2;
         }
         prev = cur; 
      }
      cout << "Case #" << i << ": " << result << endl;
   }
   return 0;
}
