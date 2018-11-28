
#include <iostream>
#include <fstream>
#include <unordered_set>

using namespace std;

int main(int argc, char **argv)
{
  ifstream ifs;
  if (argc <= 1)
    return 0;

  ifs.open(argv[1], ifstream::in);

  // number of test case
  int t;
  ifs >> t;

  for (int i = 1; i <= t; i++)
  {
    long long n = 0;
    cout << "Case #" << i << ": ";

    ifs >> n;

    if (n == 0)
    {
      cout << "INSOMNIA" << endl;
      continue;
    }

    long long c = 1;
    for (unordered_set<unsigned char> s; s.size() != 10; c++)
    {
      long long x = n * c;
      for (; x != 0; x /= 10)
	s.insert(x % 10);
    }

    cout << n * --c << endl;
  }
}
