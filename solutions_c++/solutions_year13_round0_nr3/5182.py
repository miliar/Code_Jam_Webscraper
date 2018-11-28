#include "common.h"

using namespace std;

bool is_palindrome(int x, int base = 10);

int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    exit(1);
  }

  ifstream ifs(argv[1]);

  int T;
  int fair_square_count;
  int A, B;

  ifs >> T;
  for (int i = 0; i < T; ++i)
  {
    fair_square_count = 0;
    ifs >> A >> B;

    for (int j = A; j <= B; ++j)
    {
      int j_sqrt = (int) (sqrt(j) + 0.5);
      bool is_square = (j_sqrt * j_sqrt) == j;

      if (is_palindrome(j) && is_square && is_palindrome(j_sqrt))
        ++fair_square_count;
    }

    cout << "Case #" << (i+1) << ": " << fair_square_count << endl;
  }
}

bool is_palindrome(int x, int base)
{
  int x_reverse = 0, x_orig = x;
  while (x_orig > 0)
  {
    x_reverse = x_reverse * 10 + (x_orig % 10);
    x_orig = x_orig / 10;
  }

  return x == x_reverse;
}
