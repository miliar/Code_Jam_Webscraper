#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <assert.h>

FILE *fin = fopen ("input.txt", "r");
FILE *fout = fopen ("output.txt", "w");

bool isPalindrome (int number);
int squareRoot (int number);
void testPalin (void);

int main (int argc, char **argv) {  
   int t;
   fscanf (fin, "%d", &t);
   
   int start, end;
   for (int i = 0; i < t; i++) {
      int numFair = 0;
      fscanf (fin, "%d %d", &start, &end);
      for (int j = start; j <= end; j++) {
         int root = squareRoot (j);
         if (root) {
            //if the square root exists as an integer
            if (isPalindrome (j) && isPalindrome (root)) {
               numFair++;
            }
         }
      }
      fprintf (fout, "Case #%d: %d\n", i + 1, numFair);
   }
   
   return 0;
}

bool isPalindrome (int number) {
   char buffer[105];
   memset (buffer, '\0', 105);
   sprintf (buffer, "%d", number);
   
   int length = strlen (buffer);
   
   bool palindrome = true;
   for (int i = 0; i < length/2; i++) {
      if (buffer[i] != buffer[length - 1 - i]) {
         palindrome = false;
      }
   }
   
   return palindrome;
}

//return square root if it's an integer, 0 otherwise
int squareRoot (int number) {
   double result = sqrt (number);
   
   if ((int)result == result) {
      return (int)result;
   }
   
   return 0;
}

void testPalin (void) {
   assert (isPalindrome (22) == true);
   assert (isPalindrome (222) == true);
   assert (isPalindrome (242) == true);
   assert (isPalindrome (2332) == true);
   assert (isPalindrome (25752) == true);
   assert (isPalindrome (22577522) == true);
   
   assert (isPalindrome (23) == false);
   assert (isPalindrome (233) == false);
   assert (isPalindrome (225332) == false);
   assert (isPalindrome (2254) == false);
   assert (isPalindrome (754654) == false);
}
