#include <iostream>
#include <Vector>

using namespace std;

int main()
{
  int cases, row;
  int grid[4][4];
  vector<int> choices;

    
  cin >> cases;

  for( int c = 0; c < cases; c ++ )
  {
    cin >> row;
      row--;
    choices.clear();

      for( int i = 0; i < 4; i ++ )
          for( int j = 0; j< 4; j ++ )
              cin >> grid[i][j];

    for( int col = 0; col < 4; col ++ )
      choices.push_back( grid[row][col] );

    cin >> row;
      row--;
      for( int i = 0; i < 4; i ++ )
          for( int j = 0; j< 4; j ++ )
              cin >> grid[i][j];
      
      bool isIn = false;
      vector<int> solution;
      
      for( int col = 0; col < 4; col ++ )
      {
          isIn = false;
          
          for( int i = 0; i < choices.size(); i ++ )
          {
              if( grid[row][col] == choices[i] )
                  isIn = true;
          }
          
          if( isIn )
              solution.push_back( grid[row][col] );
      }
      
      cout << "Case #" << c+1 << ": ";
      if( solution.size() > 1 )
          cout << "Bad magician!" << endl;
      else if( solution.size() == 1 )
          cout << solution[0] << endl;
      else
          cout << "Volunteer cheated!" << endl;
  }

  return 0;
}
