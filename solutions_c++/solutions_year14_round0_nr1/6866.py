#include <iostream>
#include <cstdio>

using namespace std;

int main() 
{
  // Get number of test cases
  int T, answer, tmp, guess;
  int selectedRow[4];
  cin >> T;
  for (int i=1; i<=T; i++)
    {
      // Reset match
      int match = 0;
      cin >> answer;
      // Get first card layout
      for (int j=0; j<4; j++)
        {
          for(int k=0; k<4; k++) 
            {
              if ((j+1) == answer )
                {
                  // Store selected row
                  cin >> selectedRow[k];
                } 
              else
                {
                  // Discard other rows
                  cin >> tmp;
                }
            }
        }
      // Get second answer
      cin >> answer;
      // Get second card layout
      for (int j=0; j<4; j++)
        {
          for(int k=0; k<4; k++) 
            {
              if ((j+1) == answer )
                {
                  cin >> tmp;
                  // Check if tmp is in selectedRow
                  for (int l=0; l<4; l++) 
                    {
                      if (tmp == selectedRow[l])
                        {
                          match++;
                          guess = tmp;
                        }
                    }
                } 
              else
                {
                  cin >> tmp;
                }
            }
        }
      if (match == 0)
        {
          printf("Case #%d: %s\n", i, "Volunteer cheated!");
        }
      else if (match == 1) 
        {
          printf("Case #%d: %d\n", i, guess);
        }
      else if (match > 1)
        {
          printf("Case #%d: %s\n", i, "Bad magician!");
        }
    }        
  return 0;
}
