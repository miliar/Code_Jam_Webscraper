#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int Smax;
    cin >> Smax;
    string s;
    cin >> s;
    int over = 0;
    int result = 0;
    for (int i = 0; i <= Smax; ++i)
    {
      if (s[i] == '0') {
	if (over == 0)
	  ++result;
	else
	  --over;
      } else {
	over += s[i]-'1';
      }
    }
    cout << "Case #" << i << ": " << result << endl;
  }
  return 0;
}
