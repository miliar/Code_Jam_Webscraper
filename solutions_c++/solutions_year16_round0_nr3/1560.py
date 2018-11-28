#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  int T, N, J;
  cin >> T >> N >> J;
  cout << "Case #1:" << endl;
  for (int i = 1; i <= J; ++i)
  {
    string s = "1" + string(N-2, '0') + "1";
    int j = i;
    int pos = N-2;
    while (j)
    {
      if (j%2 == 1)
      {
        s[pos] = '1';
        s[pos-1] = '1';
      }
      pos -= 2;
      j /= 2;
    }
    cout << s << " 3 4 5 6 7 8 9 10 11" << endl;
  }
}
