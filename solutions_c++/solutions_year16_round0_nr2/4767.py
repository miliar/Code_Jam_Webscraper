#include <algorithm>
#include <iterator>
#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

void flip(std::string& s, int i, int j)
{
  std::reverse(s.begin() + i, s.begin() + j + 1);
  for(int pos = i; pos <= j; pos++)
  {
    if(s[pos] == '+')
      s[pos] = '-';
    else if(s[pos] == '-')
      s[pos] = '+';
  }
}

ll solve(std::string& s)
{
  ll cnt = 0;
  int i = 0, j = s.size() - 1;
  while(i <= j)
  {
    while(s[j] == '+')
      j--;
    if(i > j)
      break;

    if(s[i] == '-')
    {
      flip(s, i, j);
      cnt++;
      continue;
    }
    
    int pos = i;
    while(s[pos] == '+')
      pos++;

    flip(s, i, pos - 1);
    cnt++;
  }

  return cnt;
}

int main()
{
  int t;
  cin >> t;

  std::string s;
  
  for(int tt = 1; tt <= t; tt++)
  {
    cin >> s;
    cout << "Case #" << tt << ": " << solve(s) << std::endl;
  }

	return 0;
}
