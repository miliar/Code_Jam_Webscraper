#include <iostream>

int main (void) {
   int n;
   std::cin >> n;
   for (int i = 1; i < n+1; ++i) {
      std::string s;
      std::cin >> s;

      std::cout << "Case #" << i << ": ";
      int letters[26] = {0};
      int soln[10] = {0};

      for (int j = 0; j < (int) s.size(); ++j) {
         letters[s[j] -'A']++;
      }

      // zero
      int size = letters['Z'-'A'];
      soln[0] = size;
      letters['Z'-'A'] -= size; 
      letters['E'-'A'] -= size;
      letters['R'-'A'] -= size;
      letters['O'-'A'] -= size; 
      
      // two
      size = letters['W'-'A'];
      soln[2] = size;
      letters['T'-'A'] -= size; 
      letters['W'-'A'] -= size;
      letters['O'-'A'] -= size;
      
      // four
      size = letters['U'-'A'];
      soln[4] = size;
      letters['F'-'A'] -= size; 
      letters['O'-'A'] -= size;
      letters['U'-'A'] -= size;
      letters['R'-'A'] -= size; 
      
      // SIX
      size = letters['X'-'A'];
      soln[6] = size;
      letters['S'-'A'] -= size; 
      letters['I'-'A'] -= size;
      letters['X'-'A'] -= size;

      // EIGHT
      size = letters['G'-'A'];
      soln[8] = size;
      letters['E'-'A'] -= size; 
      letters['I'-'A'] -= size;
      letters['G'-'A'] -= size;
      letters['H'-'A'] -= size; 
      letters['T'-'A'] -= size; 
      
      // three
      size = letters['R'-'A'];
      soln[3] = size;
      letters['T'-'A'] -= size; 
      letters['H'-'A'] -= size;
      letters['R'-'A'] -= size;
      letters['E'-'A'] -= (size * 2);

      // FIVE
      size = letters['F'-'A'];
      soln[5] = size;
      letters['F'-'A'] -= size; 
      letters['I'-'A'] -= size;
      letters['V'-'A'] -= size;
      letters['E'-'A'] -= size; 

      // seven
      size = letters['S'-'A'];
      soln[7] = size;
      letters['S'-'A'] -= size; 
      letters['E'-'A'] -= (size * 2);
      letters['V'-'A'] -= size;
      letters['N'-'A'] -= size; 
      
      // ONE
      size = letters['O'-'A'];
      soln[1] = size;
      letters['O'-'A'] -= size; 
      letters['N'-'A'] -= size;
      letters['E'-'A'] -= size;
      
      // NINE
      size = letters['I'-'A'];
      soln[9] = size;
      letters['N'-'A'] -= (size * 2); 
      letters['I'-'A'] -= size;
      letters['E'-'A'] -= size;      
      
      for (int j = 0; j < 10; j++) {
            for (int k = 0; k < soln[j]; k++) {
                std::cout << j;
            }
      }
      std::cout << "\n";
   }
}