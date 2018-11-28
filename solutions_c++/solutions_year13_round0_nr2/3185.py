#include <iostream>
#include <stdio.h>

#define UNCHECKED 0
#define SET 1
#define UNSET 2

void get_lawn(int[][100], int, int);
bool test_lawn(int[][100], int, int);

using namespace std;

int main()
{
  int T;
  int N, M;
  int lawn[100][100];
  bool success;
  

  cin >> T;

  for(int t = 1; t <= T; t++)
  {
    cin >> N >> M;

    get_lawn(lawn, N, M);
    success = test_lawn(lawn, N, M);

    if(success)
      printf("Case #%d: YES\n", t);
    else
      printf("Case #%d: NO\n", t);
    
  }

  

  return 0;
}

void get_lawn(int lawn[][100], int N, int M)
{
  for(int n = 0; n < N; n++)
  {
    for(int m = 0; m < M; m++)
    {
      cin >> lawn[n][m];
    }
  }
  
  /* debugging
  for(int n = 0; n < N; n++)
  {
    for(int m = 0; m < M; m++)
      cout << lawn[n][m] << " ";

    cout << endl;
  }
  */
}

bool test_lawn(int lawn[][100], int N, int M)
{
  for(int n = 0; n < N; n++)
  {
    for(int m = 0; m < M; m++)
    {
      int x = lawn[n][m];
      
      bool h = true;
      //check horizontal
      for(int j = 0; j < M; j++)
      {
        if(x < lawn[n][j])
        {
          h = false;
          break;
        }
      }
      
      //only check if it's impossible horizontally
      if(!h)
      {
        for(int i = 0; i < N; i++)
        {
          if(x < lawn[i][m])
          {
            //since we are only here if it already failed horizontally,
            //if it fails again we know it's impossible
            return false;
          }
        }
      }


    }
  }

  return true;

}
