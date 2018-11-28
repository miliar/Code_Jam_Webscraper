#include <iostream>

// As rotations are allowed R & C can be exchanged without changing the result
// Lets assume then R >= C

// For Richard to win:
//  R < X (straight line)
//  2C < X (L shape)
//  X|R*C
//  X>=7 (he can choose a shape with hole inside)

// Gabriel allways wins if:
//  X=1
//  X=2 & X|R*C

int main()
{
  using namespace std;
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int X, R, C;
    cin >> X >> R >> C;
    if (C > R)
      swap(R, C);
    cout << "Case #" << i << ": ";
    if (R < X || 2*C < X || R*C%X != 0 || X >= 7 || (X == 4 && R == 4 && C == 2))
      cout << "RICHARD";
    else
      cout << "GABRIEL";
    cout << endl;
  }
}