#include <iostream>
#include <vector>
#include <string>

// + is 1, - is 0
//

void parse(const std::string& s, std::vector<int>& v)
{
  v.resize(s.size());
  for ( int i = 0; i < s.size(); ++i )
  {
    if ( s[i] == '-' )
      v[i] = 0;
    else if ( s[i] == '+' )
      v[i] = 1;
  }
}

void flip(std::vector<int>& v, int n)
{
  for ( int i = 0; i <= n; ++i )
  {
    if ( v[i] == 0 )
      v[i] = 1;
    else if ( v[i] == 1 )
      v[i] = 0; 
  }
}

void arrange(std::vector<int>& v, int n, int& flips)
{
  if ( n < 0 )
    return;

  if ( v[n] == 1 )
  {
    // nothing to flip.
  }
  else
  {
    flip(v, n);
    ++flips;
  }

  if ( n > 0 )
  {
    arrange(v, n-1, flips);
  }
}

int main(int argc, char* argv[])
{
  int testcases;
  std::cin >> testcases;
  for ( int i = 0; i < testcases; ++i )
  {
    std::string s;
    std::cin >> s;
    std::vector<int> v;
    std::vector<int> cachedFlips(s.size(), -1);
    parse(s, v);
    int flips = 0;
    arrange(v, s.size() - 1, flips);
    std::cout << "Case #" << (i + 1) << ": " << flips << std::endl;
  }
  return 0;
}

