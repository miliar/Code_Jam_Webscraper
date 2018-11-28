#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int test_case = 1; test_case <= T; ++test_case)
  {
    int N, M;
    cin >> N >> M;
    vector< vector<int> > lawn(N, vector<int>(M, -1));
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < M; ++j)
	cin >> lawn[i][j];

    vector<int> x(N, 0), y(M, 0);
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < M; ++j)
      {
	x[i] = max(x[i], lawn[i][j]);
	y[j] = max(y[j], lawn[i][j]);
      }

    bool possible = true;
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < M; ++j)
	if (!((lawn[i][j] == x[i]) || (lawn[i][j] == y[j])))
	{
	  possible = false;
	  break;
	}

    cout << "Case #" << test_case << ": " << (possible ? "YES" : "NO") << endl;
  }
  return 0;
}
