#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath> 

using namespace std;


int main() {

   //num of test cases
   int test_cnt;
   
   cin >> test_cnt;

   for(int idx = 1; idx <= test_cnt; idx++) {
      double C,F,X;
      cin >> C;
      cin >> F;
      cin >> X;
      
      double time = 0;
      double base = 0;
      int i = 0; 
      while(true) {
         if ( X/(2+i*F) < (C/(2+i*F) + X/(2+(i+1)*F))){
             time = base + X/(2+i*F);
             break;
         }
         base += C/(2+i*F);
         i++;
      }
      cout << "Case #" << idx << ": ";
      printf("%.7f\n",time);
   }

   return 0;
}
