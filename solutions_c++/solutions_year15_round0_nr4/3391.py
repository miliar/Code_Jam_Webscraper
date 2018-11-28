#include<iostream>
#include <algorithm>
#include <vector>
#include<string>


using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++)
  {
    int X, R, C;
    string  result = "GABRIEL";
    cin >> X >> R >> C;

    if (R*C % X != 0)
      result = "RICHARD";

    if (X > max(R,C))
      result = "RICHARD";

    switch(X)
    {
      case 3:
        if (R == 1 || C == 1)
          result = "RICHARD";
        break;
      case 4:
        if (R <= 2 || C <= 2)
          result = "RICHARD";
        break;
    }

    cout << "Case #" << i+1 << ": " << result << endl;
  }
}
