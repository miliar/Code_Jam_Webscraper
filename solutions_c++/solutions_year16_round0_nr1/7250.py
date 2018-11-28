#include <set>
#include <iostream>

void setDigits(std::set<int>& digits, unsigned long long no)
{
  while ( no > 0 )
  {
    int dig = no % 10;
    no = no / 10;
    digits.insert(dig);
  }
}

int main(int argc, char* argv[])
{
  int testcases;
  std::cin >> testcases;
  for ( int i = 0; i < testcases; ++i )
  {
    unsigned long long n;
    std::cin >> n;
    bool cont;
    int k = 1;
    int lastTimeChangedDigits = k;
    std::set<int> digits;
    while ( cont )
    {
      std::size_t nodigsBefore = digits.size();
      setDigits(digits, n * k);
      if ( digits.size() != nodigsBefore )
      {
        lastTimeChangedDigits = k;
      }
      if ( digits.size() == 10 )
      {
        std::cout << "Case #" << (i + 1) << ": " << (n * k) << std::endl;
        break;
      }
      if ( k > lastTimeChangedDigits + 1000 )
      {
        std::cout << "Case #" << (i + 1) << ": INSOMNIA" << std::endl;
        break;
      }
      ++k;
    }
  }
}

