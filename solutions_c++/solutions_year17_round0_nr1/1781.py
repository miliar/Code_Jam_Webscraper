#include <iostream>
#include <string>

using namespace std;
int main()
{
  const int flip = '-' ^ '+';
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    int cn = 0;
    string s; int k; cin >> s >> k;
    int l = s.length();
    for (int i = 0; i < l; i++)
    {
      if (s[i] == '-')
      {
        if (i + k > l)
        {
          cn = -1;
          break;
        }
        else {
          cn += 1;
          for (int j = 0; j < k; j++)
          {
            s[i+j] ^= flip;
          }
        }
      }
    }
    cout << "Case #" << ii << ": ";
    if (cn < 0)
    {
      cout << "IMPOSSIBLE" << endl;
    }
    else   
    {
      cout << cn << endl;
    }
  }
  return 0;
}