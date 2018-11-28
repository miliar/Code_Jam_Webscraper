#include <fstream>
#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
  ifstream in(argv[1]);
  unsigned int N;
  in >> N;
  in.ignore();

  for (unsigned int n = 0; n < N; ++n)
  {
    unsigned int X, R, C;
    in >> X >> R >> C;
    cout << "Case #"<<n+1<<": ";

    bool gabriel_wins = false;
    switch (X)
    {
      case 1:
        gabriel_wins = true;
        break;
      case 2:
        if (R % 2 == 0 || C % 2 == 0)
          gabriel_wins = true;
        break;
      case 3:
        if (R % 3 == 0 && C >= 2)
          gabriel_wins = true;
        if (C % 3 == 0 && R >= 2)
          gabriel_wins = true;
        break;
      case 4:
        if (R % 4 == 0 && C >= 3)
          gabriel_wins = true;
        if (C % 4 == 0 && R >= 3)
          gabriel_wins = true;
        break;
    }

    if (gabriel_wins)
      cout << "GABRIEL";
    else
      cout << "RICHARD";
    cout << endl;
  }
}