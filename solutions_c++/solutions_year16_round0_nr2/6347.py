#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <string>
#include <unistd.h>
#include <stdint.h>

void checkDigit(std::string& nbSeen, int nb)
{
  std::string result = std::to_string(nb);
  std::size_t found;

  for (uint64_t i = 0; i < result.size(); i++) {
    if ((found = nbSeen.find(result[i])) == std::string::npos)
      nbSeen += result[i];
  }
}


using namespace std;

int serve(std::string& n) {
  std::string tmp;
  std::size_t found;
  int flip = 0;

  while (true)
  {
    if ((found = n.find('-') == std::string::npos))
      break;
    if (n[0] == '+')
    {
      int i = 0;
      ++flip;
      while (n[i] == '+')
        {
          n[i] = '-';
          ++i;
        }
    } else if (n[0] == '-') {
      int i = 0;
      ++flip;
      while (n[i] == '-')
        {
          n[i] = '+';
          ++i;
        }
    }
  }
  return flip;
}

int main() {
  int t;
  int flip;
  std::string n;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n; // read n and then m.
    flip = serve(n);
    cout << "Case #" << i << ": " << flip << endl;
  }
  return (0);
}
