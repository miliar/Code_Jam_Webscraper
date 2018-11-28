#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

bool palindromes(const int x)
{
  int a = x;
  int b = 0;
  while (a != 0) {
    b = b * 10 + a % 10;
    a = a / 10;
  }
  return (b == x);
}

int main(int argc, char *argv[])
{
  ifstream fin("C-small-attempt0.in.txt");
  int cases;
  int cnt = 0;

  fin >> cases;
  while (++cnt <= cases) {
    int n = 0;
    int A, B;
    fin >> A >> B;
    int a = (int)ceil(sqrt(A));
    int b = (int)floor(sqrt(B));

    for (int i = a; i <= b; ++i) {
      if (palindromes(i) && palindromes(i * i))
	++n;
    }
    cout << "Case #" << cnt << ": " << n << endl;
  }
  fin.close();
  return 0;
}
