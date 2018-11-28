#include <iostream>

int main(int argc, char const *argv[])
{
  using namespace std;

  int tc;
  cin >> tc;

  for (int z = 0; z < tc; ++z)
  {
    int answer = 0, counter = 0;
    int r1, r2;
    cin >> r1;

    int mem1[4], mem2[4];

    memset(mem1, -1, sizeof(mem1));
    memset(mem2, -1, sizeof(mem2));

    for (int row = 0; row < 4; ++row)
    {
      for (int col = 0; col < 4; ++col)
      {
        int num = 0;
        if ( row == r1-1 )
          cin >> mem1[col];
        else
          cin >> num;

      }
    }

    cin >> r2;

    for (int row = 0; row < 4; ++row)
    {
      for (int col = 0; col < 4; ++col)
      {
        int num = 0;
        if ( row == r2-1 )
          cin >> mem2[col];
        else
          cin >> num;
      }
    }

    for (int k = 0; k < 4; ++k)
    {
      for (int p = 0; p < 4; ++p)
      {
        if ( mem1[k] == mem2[p] ) {
          answer = mem1[k];
          counter++;
        }
      }
    }

    if ( counter == 1 )
      cout << "Case #" << z+1 << ": " << answer;
    else if ( counter > 1 )
      cout << "Case #" << z+1 << ": " << "Bad magician!";
    else if ( counter == 0 )
      cout << "Case #" << z+1 << ": " << "Volunteer cheated!";

    cout << endl;
  }
  return 0;
}