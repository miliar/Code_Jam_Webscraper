#include <iostream>
const int N = 20;
int h[2][N];
using namespace std;
int main() {
  int tt;
  cin >> tt;
  for(int t = 1; t <= tt; ++t){
    int q1;
    cin >> q1;
    for(int i = 1; i <= 16; ++i)
    {
      h[0][i] = 0;
      h[1][i] = 0;
    }
    for(int i = 1; i < q1; ++i)
    {
      for(int j = 1; j <= 4; ++j)
      {
        int x;
        cin >> x;
      }
    }

    for(int j = 1; j <= 4; ++j)
    {
      int x;
      cin >> x;
      h[0][x] = 1;
    }

    for(int i = q1 + 1; i <= 4; ++i)
    {
      for(int j = 1; j <= 4; ++j)
      {
        int x;
        cin >> x;
      }
    }

    int q2;
    cin >> q2;
    for(int i = 1; i <= 4; ++i)
    {
      if(i == q2) {
        for(int j = 1; j <= 4; ++j)
        {
          int x;
          cin >> x;
          h[1][x] = 1;
        }
      }
      else {
        for(int j = 1; j <= 4; ++j)
        {
          int x;
          cin >> x;
        }
      }
    }
    int nr = 0;
    for(int i = 1; i <= 16; ++i)
    {
      nr += (h[0][i] == h[1][i] && h[0][i] == 1);
    }

    if(nr == 0) {
      cout << "Case #" << t << ": Volunteer cheated!\n";
    }
    else if (nr == 1) {
      for(int i = 1; i <= 16; ++i)
      {
        if(h[0][i] == h[1][i] && h[0][i]) {
          cout << "Case #" << t << ": " << i << '\n';
          break;
        }
      }
    } else {
      cout << "Case #" << t << ": Bad magician!\n";
    }
  }

  return 0;
}
