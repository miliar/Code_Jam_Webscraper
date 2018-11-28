#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

static const char *kRichard = "RICHARD";
static const char *kGabriel = "GABRIEL";

int main(void)
{
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; ++i)
  {
    int x, r, c;
    cin >> x >> r >> c;
    string answer;
    // Create an X-omino with a 1x1 gap in the center
    if (x >= 7)
    {
      answer = kRichard;
    }
    // Create an "L" that won't fit on the board
    // e.g. x, r, c = 5, 2, 4
    // Board:
    // * * * *
    // * * * *
    // Richard chooses
    // * * *
    // *
    // *
    else if (x > 2 * std::min(r, c))
    {
      answer = kRichard;
    }
    // See if we can isolate a corner
    // e.g. x, r, c = 4, 2, 4
    // Board:
    // * * * *
    // * * * *
    // Richard chooses a "T" that can't be rotated
    // * * *
    //   *
    // If the board is longer, Gabriel could
    // potentially shift the piece to fill it in with another
    // piece
    // For simplicity, suppose r <= c
    // e.g. x, r, c = 6, 3, 8
    // * * * *
    //   *
    //   *
    // * x x x x * * *
    // * * x * * * * *
    // * * x * * * * *
    // However, we're going to block off r - 1 blocks
    // and shifting adds intervals of r
    // meaning the isolated part is always going to be === r - 1 mod r
    // or (1 - r) mod r if Gabriel reflects the piece
    // and thus can't be filled since x === 0 mod r (being 2 x r)
    else if (x == 2 * std::min(r, c) && x > 2)
    {
      answer = kRichard;
    }
    else if ((r * c) % x != 0)
    {
      answer = kRichard;
    }
    else
    {
      answer = kGabriel;
    }
    cout << "Case #" << i+1 << ": " << answer << "\n";
  }
}