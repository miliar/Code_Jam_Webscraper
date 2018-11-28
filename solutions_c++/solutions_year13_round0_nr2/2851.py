#include <iostream>
using namespace std;

int  lawn [100][100];
int  model[100][100];
int  caseCnt, M, N;
bool fail;

int main( )
{
  cin >> caseCnt;
  for ( int caseNr = 1; caseNr <= caseCnt; ++caseNr )
  {
    fail = false;
    cin >> N >> M;
    for ( int i = 0; i < N; ++i )
      for ( int j = 0; j < M; ++j )
      {
        cin >> lawn[i][j];
        model[i][j] = 100;
      }
    // rows
    for ( int i = 0; i < N; ++i )
    {
      int maxi = 0;
      for ( int j = 0; j < M; ++j )
        maxi = max( maxi, lawn[i][j] );
      for ( int j = 0; j < M; ++j )
        model[i][j] = min( maxi, model[i][j] );
    }
    // cols
    for ( int i = 0; i < M; ++i )
    {
      int maxi = 0;
      for ( int j = 0; j < N; ++j )
        maxi = max( maxi, lawn[j][i] );
      for ( int j = 0; j < N; ++j )
        model[j][i] = min( maxi, model[j][i] );
    }
    // check
    for ( int i = 0; i < N; ++i )
      for ( int j = 0; j < M; ++j )
        if ( model[i][j] != lawn[i][j] )
          goto fail;
    cout << "Case #" << caseNr << ": YES" << endl;
    continue;
    fail:
    cout << "Case #" << caseNr << ": NO" << endl;
  }
  return 0;
}