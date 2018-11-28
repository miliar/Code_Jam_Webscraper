#include <iostream>
using namespace std;
int main(){
   int n;
   cin >> n;
   for(int x = 0; x < n; x++){
      long long input;
      cin >> input;
      cout << "Case #" << x + 1 << ": ";
      if(input == 0){
         cout << "INSOMNIA" << endl;
      } else {
         int digit[10] = { 0 };
         int digitCheck = 0;
         long long iteration = 1;
         long long count = input;
         long long temp;
         while(true){
            temp = count*iteration;
            while(temp != 0){
               int moddy = temp % 10;
               if(digit[moddy] == 0){
                  digit[moddy]++;
                  digitCheck++;
                  //cout << "got digit " << moddy << endl;
               }
               temp /= 10;
            }
            if(digitCheck == 10){
               cout << iteration * count << endl;
               break;
            }
            iteration++;
         }
      }
   }
   return 0;
}
