#include <cstdio>
#include <cstdint>
#include <inttypes.h>
#include <set>

using namespace std;


uint64_t solve(uint64_t startNumber, uint32_t MAX_ITERS)
{
  if (startNumber == 0)
    return 0;

  bool digits[10];

  auto isSolved = [&]()
  {
    auto result = true;
    for (int i = 0; i < 10; ++i)
      result &= digits[i];
    return result;
  };

  auto addDigits = [&](uint64_t number)
  {
    while (number)
    {
      digits[number % 10] = true;
      number /= 10;
    }
  };

  uint64_t number = startNumber;
  for (int i = 1; i < MAX_ITERS; ++i)
  {
    number = startNumber * i;
    addDigits(number);
    if (isSolved())
      return number;
  }

  return 0;
}

int main()
{
  uint64_t numTestCases;

  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%" SCNu64, &numTestCases);

  for (uint64_t caseIdx = 0; caseIdx < numTestCases; ++caseIdx)
  {
    uint64_t startNumber;
    scanf("%" SCNu64, &startNumber);

    printf("Case #%" SCNu64 ": ", caseIdx + 1);
    if (auto result = solve(startNumber, 1 << 32 - 1))
    {
      printf("%" SCNu64 "\n", result);
    }
    else
    {
      printf("INSOMNIA\n");
    }
  }
}