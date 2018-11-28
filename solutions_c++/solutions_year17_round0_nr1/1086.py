#include<iostream>

using namespace std;
int main() {
   int test;
   cin >> test;
   int i = 1;
   while(test--) {
      int count = 0;
      string s;
      cin >> s;
      int size;
      cin >> size;
      int n = s.size()-size+1;
      int j;
      for(j=0; j<n; j++){
         int temp = j+size;
         if(s[j] == '+') continue;
         count ++;
         int k = j;
         while(k<temp) {
           if(s[k] == '-') s[k] = '+'; 
           else s[k] = '-';
           k++;
         }
         //cout << s << endl;
      }
      bool flag = true;
      for(;j<s.size(); j++) {
         if(s[j] == '-') {
            flag = false;
            break;
         }
      }
      if(flag) {
         cout << "Case #" << i << ": "<< count << endl;
      } else {
         cout << "Case #" << i << ": IMPOSSIBLE" << endl;
      }
      i++;
   }
   return 0;
}
