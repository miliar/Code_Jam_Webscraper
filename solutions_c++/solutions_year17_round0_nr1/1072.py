#include <iostream>
#include <string>
#include <stdexcept>

char flip(const char c) {
  char ret;

  switch (c) {
    case '+': 
      ret = '-';
      break;
    case '-':
      ret = '+';
      break;
    default:
      throw std::invalid_argument{"c should be either + or -"};
  }

  return ret;
}

int solve(const std::string &S, int K)
{
  std::string cur = S;

  int count = 0;

  int off = 0;
  int remaining = S.size();

  while (remaining > 0)
  {
    if (cur[off] == '+')
    {
      ++off; --remaining;
    }
    else
    {
      if (remaining < K) return -1;

      for (int i = 0; i < K; ++i)
      {
        cur[off + i] = flip(cur[off +i]);
      }

      ++count;
    }
  }

  return count;
}

int main(int argc, char **argv) 
{
  int T = 0;

  std::cin >> T;

  for (int i = 0; i < T; ++i)
  {
    std::string S;
    int K;

    std::cin >> S >> K;

    int count = solve(S, K);

    std::cout << "Case #" << (i + 1) << ": ";

    if (count >= 0) 
    {
      std::cout << count;
    }
    else
    {
      std::cout << "IMPOSSIBLE"; 
    }

    std::cout << std::endl;
  }

  return 0;
}
