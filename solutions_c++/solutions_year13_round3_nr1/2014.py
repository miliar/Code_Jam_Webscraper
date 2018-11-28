#include <cstdio>
#include <cstdlib>
#include <cstring>

bool isConsonant (char letter) {
   bool returnValue = true;
   if (letter == 'a' || letter == 'e' || letter == 'i' ||
       letter == 'o' || letter == 'u') {
      returnValue = false;
   }
   return returnValue;
}

long long numSubstrings (int length) {
   long long returnValue = length * (length+1) / 2;
   
   return returnValue;
}

int main (int argc, char **argv) {
   FILE *fin = fopen ("input.txt", "r");
   FILE *fout = fopen ("output.txt", "w");
   
   int T;
   fscanf (fin, "%d", &T);
   
   char word[1000005];
   int nValue = 0;
   
   for (int i = 0; i < T; i++) {
      int n, length;
      fscanf (fin, "%s %d", word, &n);
      length = strlen (word);
      //printf ("%s has length %d\n", word, length);
      
      int start = 0;
      int pos = 0;
      int numConsonants = 0;
      int prevEnd = -1;
      long long nValue = numSubstrings (length);
      //printf ("Total of %lld...\n", nValue);
      while (pos < length) {
         if (isConsonant (word[pos])) {
            numConsonants++;
         } else {
            numConsonants = 0;
         }
         if (numConsonants == n) {
            //substring from start to pos-1 inclusive is removed
            nValue -= numSubstrings (pos-start);
            int overlap = prevEnd - start + 1;
            prevEnd = pos - 1;
            nValue += numSubstrings (overlap);
            //printf ("...removed %lld, compensated for %lld overlap\n", numSubstrings (pos-start), numSubstrings (overlap));
            start = pos - (n-2);
            pos = start - 1;
            numConsonants = 0;
         } else if (pos == length - 1) {
            nValue -= numSubstrings (pos-start+1);
            int overlap = prevEnd - start + 1;
            nValue += numSubstrings (overlap);
            //printf ("...removed %lld, compensated for %lld overlap\n", numSubstrings (pos-start+1), numSubstrings (overlap));
         }
         pos++;
      }
      
      //printf ("Final nValue = %lld\n\n", nValue);
      fprintf (fout, "Case #%d: %lld\n", i+1, nValue);
      nValue = 0;
   }
   
   //system ("pause");
   return EXIT_SUCCESS;
}
