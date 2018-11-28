#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <vector>

using namespace std;

bool IsPalindrome(unsigned long long int number){
    unsigned long long int reversed = 0;
    unsigned long long int k = number;
 
    while (k > 0) {
        reversed = 10 * reversed + k % 10;
        k /= 10;
    }
    return number == reversed;
}


int createPalindrome(unsigned long long int input, bool isOdd) {
   unsigned long long int n = input;
   unsigned long long int palin = input;

   if (isOdd)
      n /= 10;
    
   while (n > 0) {
      palin = palin * 10 + (n % 10);
      n /= 10;
   }

   return palin;
}



int main()
{
   // gvog @ Saturday  April, 13
   // read in the number of test cases:
   int t = 0;
   scanf("%d\n", &t);

   for (int it = 0; it < t; it++){
      // For each test case, read in a line containing three integers:
      unsigned long long int min, max;
      scanf("%lld %lld\n", &min, &max);
      int nfound = 0;
      unsigned long long int result = 0;
      unsigned long long int number = 0;     

      for (int j = 0; j < 2; j++) {
         bool isOdd = (j % 2 == 0);
         unsigned long long int i = 1;
    
         while ((number = createPalindrome(i, isOdd)) <= max) {
            if (IsPalindrome(number) && IsPalindrome(number*number)){
               if (number*number <= max && number*number >= min)
                  nfound ++;
                  //cout << "Palin: " << number*number << endl;
            }
            i ++;
         }
      }

      // write the result:
      cout << "Case #" << it+1 <<": " << nfound << "\n";
   }

   return 0;
}


