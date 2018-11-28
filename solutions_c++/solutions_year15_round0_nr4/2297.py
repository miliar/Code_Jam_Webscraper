#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

int main()
{
  int N;
  cin >> N;
  getchar();

  for (int n = 0; n < N; ++n)
  {
    int x, r, c;
    cin >> x >> r >> c;

    bool res = false;
    switch (x)
    {
    case 1:  
      break;
    case 2: 
      if (r*c < 2 || r*c%2 != 0) 
        res = true;
      break;
    case 3:
      if (r == 1 || c == 1 || r*c % 3 != 0)
        res = true;
      break;
    case 4:
      if (r*c < 12)
        res = true;
      break;
    default:
      break;
    }

    string answer;
    if (res) answer = "RICHARD";
    else answer = "GABRIEL";
    cout << "Case #" << n + 1 << ": " << answer;
    cout << endl;
  }
  return 0;
}