#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

void main2()
{
  long long int B, M;
  cin >> B >> M;
  if (M > (1ll<<(B-2)))
  {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  cout << "POSSIBLE" << endl;
  int matrix[B][B];
  for (int i=0; i<B; i++)
    for (int j=0; j<B; j++)
      if (j > i)
        matrix[i][j] = 1;
      else
        matrix[i][j] = 0;
  
  if (M < (1ll<<(B-2)))
  {
    matrix[0][B-1] = 0;
    for (int i=1; i<B-1; i++)
      if (M & (1ll << (B-2-i)))
        matrix[0][i] = 1;
      else
        matrix[0][i] = 0;
  }
  
  for (int i=0; i<B; i++)
  {
    for (int j=0; j<B; j++)
      cout << matrix[i][j];
    cout << endl;
  }
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
