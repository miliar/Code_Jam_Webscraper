#include <iostream>
#include <string>
#include <stdexcept>

unsigned int digit(char c)
{
  unsigned int result = c - '0';
  if (result > 9)
  {
    throw std::logic_error("Not a digit!");
  }
  return result;
}

unsigned int invites_needed(char const * begin, char const * end)
{
  unsigned int standing = 0;
  unsigned int wanted = 0;
  unsigned int needed = 0;
  for (char const * current = begin; current < end; ++current)
  {
    if (standing < wanted)
    {
      needed += wanted - standing;
      standing = wanted;
    }
    standing += digit(*current);
    wanted++;
  }
  return needed;
}


int main(int, char**)
{
  unsigned nCases = 0;
  std::cin >> nCases;
  for (unsigned cCase = 1; cCase <= nCases; ++cCase)
  {
    unsigned maxShy = 0;
    std::string shynessConfig;
    std::cin >> maxShy >> shynessConfig;
    std::cout << "Case #" << cCase << ": "
      << invites_needed(shynessConfig.c_str(),
          shynessConfig.c_str() + shynessConfig.size())
      << std::endl;
  }
  return 0;
}


