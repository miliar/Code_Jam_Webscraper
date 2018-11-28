// Google Code Jam 2013
// Problem C
// Clément Pellegrini - clement@pelleg.fr
#include <string>
#include <iostream>
#include <fstream>
#include <list>
#include <cmath>

bool is_palindrome(std::size_t n);

int main(int argc, char *argv[])
{
  if (argc != 2)
    return 2;

  std::string arg = argv[1];

  std::ifstream file (arg.c_str());
  std::size_t nbelts;
  std::string nbeltsstr;
  std::string lowerstr, upperstr;
  std::size_t lower, upper;
  file >> nbeltsstr;
  nbelts = std::stoi(nbeltsstr);

  std::list<std::pair<std::size_t, std::size_t>> inputs;



  for (int i = 0; i < nbelts; ++i)
  {
    file >> lowerstr >> upperstr;
    lower = std::stoi(lowerstr);
    upper = std::stoi(upperstr);
    inputs.push_back (std::pair<std::size_t, std::size_t> (lower, upper));
  }
  int cases = 0;
  for (auto elt : inputs)
  {
    cases++;
    int count = 0;
    // std::cout << elt.first << " " << elt.second << std::endl;
    for (int j = elt.first; j <= elt.second; j++)
    {
      if (is_palindrome(j))
      {
        double sqrtD = sqrt(j);
        if (ceil(sqrtD) == sqrtD && is_palindrome(sqrtD))
        {
          count++;
        }
      }
      // Case #x: y
    }
    std::cout << "Case #" << cases << ": " << count << std::endl;
  }
    return 0;
}

bool is_palindrome(std::size_t n)
{
  std::size_t temp, reverse;
  reverse = 0;
  temp = n;

  while( temp != 0 )
  {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
  }
  return (reverse == n);
}
