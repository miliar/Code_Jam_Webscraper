#include <iostream>

using std::cout;
using std::cin;
using std::endl;

#define MATRIX_SIZE     4
#define CHEATER         0
#define BAD_MAGICIAN    (-1)

// return 0 cheater
// return -1 bad magician
// return between 1 to 16 - success
int do_test_case()
{
   int guess_1;
   cin >> guess_1;

   int matrix_1[MATRIX_SIZE][MATRIX_SIZE];
   for (int i = 0; i < MATRIX_SIZE; ++i){ for (int j = 0; j < MATRIX_SIZE; ++j) { cin >> matrix_1[i][j]; } }

   int guess_2;
   cin >> guess_2;

   int matrix_2[MATRIX_SIZE][MATRIX_SIZE];
   for (int i = 0; i < MATRIX_SIZE; ++i){ for (int j = 0; j < MATRIX_SIZE; ++j) { cin >> matrix_2[i][j]; } }

   // do the matching
   int* ptr_row_1 = matrix_1[guess_1-1];
   int* ptr_row_2 = matrix_2[guess_2-1];

   int matches = 0;
   int actual_value = -1;
   for (int i = 0; i < MATRIX_SIZE; ++i)
   {
      for (int j = 0; j < MATRIX_SIZE; ++j)
      {
         if (ptr_row_1[i] == ptr_row_2[j])
         {
            actual_value = ptr_row_1[i];
            matches++;
         }
      }
   }

   if (matches == 0)
   {
      return CHEATER;
   }
   else if (matches == 1)
   {
      return actual_value;
   }

   return BAD_MAGICIAN;
}

int main()
{
   int T = 0;
   cin >> T;

   for (int test_case = 1; test_case <= T; ++test_case)
   {
      int result = do_test_case();
      cout << "Case #" << test_case << ": ";
      if (result == CHEATER)
      {
         cout << "Volunteer cheated!";
      }
      else if (result == BAD_MAGICIAN)
      {
         cout << "Bad magician!";
      }
      else
      {
         cout << result;
      }
      cout << endl;
   }

   return 0;
}
