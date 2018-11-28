#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <queue>
#include <stdio.h>
#include <math.h>

//////////////////////////////////////////////////
// std::map<std::string, std::vector<int>> map; //
// std::vector<int> v;                          //
// v.push_back(1);                              //
// v.push_back(2);                              //
// v.push_back(3);                              //
// map["one"] = v;                              //
//                                              //
// for(const auto& kvp : map)                   //
//   {                                          //
//     std::cout << kvp.first << std::endl;     //
//                                              //
//     for(auto v : kvp.second)                 //
//       {                                      //
//         std::cout << v << std::endl;         //
//       }                                      //
//   }                                          //
//////////////////////////////////////////////////

using namespace std;

int validateLawn(const int NUM_ROWS,
                 const int NUM_COLUMNS,
                 const int * const max_rows,
                 const int * const max_cols,
                 const int * const lawn)
{
  for (int i = 0; i < NUM_ROWS; ++i)
    {
      const int row_max = max_rows[i];
      for (int j = 0; j < NUM_COLUMNS; ++j)
        {                 
          const int idx_to_check = i * NUM_COLUMNS + j;
          const int value = lawn[idx_to_check];
          if(value < row_max)        // If it's smaller than the maximum in the row...
            if(value != max_cols[j]) // Then it must be the largest of the column
              return 0;
        }
    }
  return 1;

}

inline int rowMaximum(const int NUM_ROWS,
                      const int NUM_COLUMNS,
                      const int row_to_check,
                      const int * const lawn)
{
  const int * const first_element_in_row = lawn + row_to_check * NUM_COLUMNS;
  int max = first_element_in_row[0];
  for (int i = 1; i < NUM_COLUMNS; ++i)
    {
      const int candidate = first_element_in_row[i];
      max = candidate > max ? candidate : max;
    }
  return max;
}

inline int colMaximum(const int NUM_ROWS,
                      const int NUM_COLUMNS,
                      const int col_to_check,
                      const int * const lawn)
{
  const int * const first_element_in_column = lawn + col_to_check;
  int max = first_element_in_column[0];
  for (int i = 1; i < NUM_ROWS; ++i)
    {
      const int candidate = first_element_in_column[i * NUM_COLUMNS];
      max = candidate > max ? candidate : max;
    }
  return max;
}

int main(int argc, char *argv[])
{

  int numCases;
  cin >> numCases;

  if(numCases)
    {
      cin.get(); // New line
      
      // Case Loop
      for (int _case = 0; _case < numCases; ++_case)
        {
          int N;
          int M;

          cin >> N;
          cin >> M;

          //int * lawn = new int[N*M];
          int lawn[N*M];

          // Fill Lawn Heights
          for (int i = 0; i < N; ++i)
            {
              for (int j = 0; j < M; ++j)
                {
                  cin >> lawn[i*M + j];
                  //cout << board[i*4 + j];
                }
              //cout << endl;
            }

          // Validate Lawn Heights
          //int * max_rows = new int[N];
          //cout << N;
          //int * max_cols = new int[M];
          //cout << M;
          int max_rows[N];
          int max_cols[M];

          int valid;

          //          cout << "Rows' Max\n";
          for (int i = 0; i < N; ++i)
            {
              max_rows[i] = rowMaximum(N, M, i, lawn);
              //              cout << i << ": " << max_rows[i] << endl;
            }

          //          cout << "Cols' Max\n";
          for (int j = 0; j < M; ++j)
            {
              max_cols[j] = colMaximum(N, M, j, lawn);
              //              cout << j << ": " << max_cols[j] << endl;
            }

          valid = validateLawn(N, M, max_rows, max_cols, lawn);

          if(valid)
            cout << "Case #" << _case+1 << ": YES\n";
          else
            cout << "Case #" << _case+1 << ": NO\n";

          // delete [] max_cols;
          // delete [] max_rows;
          // delete [] lawn;
        }
    }
  return 0;
}
