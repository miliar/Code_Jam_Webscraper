// mars.ma
#include <iostream>

using namespace std;

int main(void)
{
  int testcase;  cin >> testcase;
  for (int tc = 1; tc <= testcase; ++tc) {
    uint a, b, k;  cin >> a >> b >> k;
    int result = 0;
    for (uint i = 0; i < a; ++i) {
      for (uint j = 0; j < b; ++j) {
        result += ((uint)(i&j) < k);
      }
    }

    cout << "Case #" << tc << ": " << result << endl;
  }

  return 0;
}

