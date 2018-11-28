#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;

int r[2016];

string d[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int order[] = {0, 2, 6, 4, 8, 3, 1, 5, 7, 9};
char c[] = {'Z', 'W', 'X', 'U', 'G', 'H', 'O', 'F', 'S', 'I'};
int ph[10];

int main() {
   int t, x, ii, i, j, k, rt;
   string s;
   scanf("%d", &t);
   for (x = 1; x <= t; x++) {
      cin >> s;
      for (ii = 0; ii < 10; ii++) {
         i = order[ii];
         ph[i] = 0;
         for (j = 0; j < s.length(); j++) {
            if (s[j] == c[ii])
               ph[i]++;
         }
         for (j = 0; j < d[i].length(); j++) {
            rt = 0;
            for (k = 0; k < s.length() && rt < ph[i]; k++) {
               if (s[k] == d[i][j]) {
                  s[k] = '.';
                  rt++;
               }
            }
         }
         //cout << i << " " << s << " ph[i]: " << ph[i] << endl;
      }
      cout << "Case #" << x << ": ";
      for (i = 0; i < 10; i++) {
         for (j = 0; j < ph[i]; j++) {
            cout << i;
         }
      }
      cout << endl;
   }
   return 0;
}
