#include <iostream>
#include <string>
#include <algorithm>
using namespace std;// DONT LOOK AT ME
int main(){
   int n;
   cin >> n;
   for(int x = 0; x < n; x++){
      string input;
      cin >> input;
      reverse(input.begin(), input.end());
      //cout << input << endl;
      cout << "Case #" << x + 1 << ": ";
      // lol just iterate and count the sign changes from bottom
      int flips = 0; 
      char lastChar = '+';
      for(string::iterator it = input.begin(); it != input.end(); ++it){
         if(*it != lastChar){
            flips++;
            lastChar = *it;
         }
      }
      cout << flips<<endl;
      
   }
   return 0;
}
