// Problem B. Lawnmower
// By gvaf

#include <iostream>
using namespace std;

#define MAX_SIZE 120
#define MINIMUM_VALUE -1
int pattern[MAX_SIZE][MAX_SIZE];

bool isPossible(int N, int M);

int main()
{
 int T;

 cin >> T;

 for(int testID = 1; testID <= T; ++testID)
 {
   int N, M;

   cin >> N >> M;

   for(int r = 0; r < N; ++r)
     for(int c = 0; c < M; ++c)
       cin >> pattern[r][c];

   bool result = isPossible(N, M);

   cout << "Case #" << testID << ": " << (result ? "YES" : "NO") << endl;
 }

 return 0;
}

bool isPossible(int N, int M)
{
 int maxRows[MAX_SIZE];
 int maxCols[MAX_SIZE];

 for(int i = 0; i < N; ++i)
    maxRows[i] = MINIMUM_VALUE;

 for(int i = 0; i < M; ++i)
    maxCols[i] = MINIMUM_VALUE;

 for(int r = 0; r < N; ++r)
   for(int c = 0; c < M; ++c)
    {
     if( pattern[r][c] > maxRows[r] )
        maxRows[r] = pattern[r][c];

     if( pattern[r][c] > maxCols[c] )
        maxCols[c] = pattern[r][c];
    }

 for(int r = 0; r < N; ++r)
   for(int c = 0; c < M; ++c)
    {
      bool isTrimmable = (pattern[r][c] >= maxRows[r]) ||
                         (pattern[r][c] >= maxCols[c]);

      if( !isTrimmable ) return false;
    }

 return true;
}
