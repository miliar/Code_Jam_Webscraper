#include <iostream>
#include <sstream>
#include <string>

using namespace std;

string solve() {
   int cards1[16];
   int row1;
   cin >> row1;
   for (int i = 0; i < 16; i++) {
      if ((i+1) % 4 == 0) {
         cin.get();
      }
      cin >> cards1[i];
   }

   int cards2[16];
   int row2;
   cin >> row2;
   for (int i = 0; i < 16; i++) {
       if ((i+1) % 4 == 0) {
          cin.get();
       }  
       cin >> cards2[i];
   }
   
   int matchCount = 0; 
   int voluntNumber = -1;
   for (int i = 0; i < 4; i++) {
      int c1 = cards1[(row1-1)*4 + i];
      for (int j = 0; j < 4; j++) {
         int c2 = cards2[(row2-1)*4 + j];
         if (c1 == c2) {
            voluntNumber = c1;
            matchCount++;
            break;
         }
      }
   }  
 
   if (matchCount == 1) { 
      ostringstream str;
      str << voluntNumber;
      return str.str();
   }
   if (matchCount == 0) 
      return "Volunteer cheated!";
   return "Bad magician!"; 
}

int main(int argc, char ** argv) {

   int cases;
   cin >> cases;
   for (int i = 0; i < cases; i++) {
      cout << "Case #" << i+1 << ": " << solve() << endl;
   }

   return 0;
}
