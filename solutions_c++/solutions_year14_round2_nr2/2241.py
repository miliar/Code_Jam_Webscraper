#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int A, B, K;
    int res = 0;
    cin >> A >> B >> K;
    for (int j = 0; j < A; ++j)
      for (int k = 0; k < B; ++k)
	if ((j&k) < K)
	  ++res;
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}
