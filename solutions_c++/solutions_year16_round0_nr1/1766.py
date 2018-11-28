#include <iostream>
#include <bitset>
#include <string>

using namespace std;

int main(void)
{
  int N;
  cin >> N;
  for (int C = 1; C <= N; ++C)
  {
    cout << "Case #" << C << ": ";
    int64_t K, R = 0, R2;
    cin >> K;
    if (K == 0)
    {
      cout << "INSOMNIA" << endl;
      continue;
    }
    bitset<10> digits;

    while (!digits.all())
    {
      R += K;
      R2 = R;
      while (R2)
      {
        int digit = R2%10;
        R2 /= 10;
        digits[digit] = true;
      }

    }

    cout << R << endl;
  }
}
