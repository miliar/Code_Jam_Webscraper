#include <iostream>

using namespace std;

// count variation of sign
int main(void)
{
  unsigned int t;
  cin >> t;
  for (int i = 1; i <= t; i++)
  {
    std::string stack;
    cin >> stack;
    char last = stack[0];
    long changes = 0;
    for (unsigned int x = 0; x < stack.length (); x++)
    {
      if (stack[x] != last)
	changes++;

      last = stack[x];
    }
    if (last == '-') changes++;

    cout << "Case #" << i << ": " << changes << endl;
  }

  return 0;
}
