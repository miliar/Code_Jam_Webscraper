#include <iostream>
#include <vector>
#include <cstdint>
#include <cstddef>

using namespace std;

int main()
{
  uint32_t nCases;
  vector<bool> numbersSeen(10, false);
  uint32_t numbersToSee = 10;
  cin >> nCases;
  for (int _case = 1; _case <= nCases; ++_case)
  {
    uint64_t N;
    cin >> N;
    uint64_t curNumber = 0;
    for (int i = 1; numbersToSee > 0 ; ++i)
    {
      uint64_t tmp = N*i;
      if (tmp == curNumber) { curNumber = 0; break; }
      curNumber = tmp;
      while (tmp > 9)
      {
        if (!numbersSeen[tmp%10])
          numbersToSee--;
        if (numbersToSee == 0) break;
        numbersSeen[tmp % 10] = true;
        tmp /= 10;
      }
      if (numbersToSee == 0) break;
      if (!numbersSeen[tmp])
        numbersToSee--;
      if (numbersToSee == 0) break;
      numbersSeen[tmp] = true;
    }
    cout << "Case #" << _case << ": ";
    if (curNumber == 0)
      cout << "INSOMNIA" << endl;
    else cout << curNumber << endl;
    numbersSeen.assign(10, false);
    numbersToSee = 10;
  }
}
