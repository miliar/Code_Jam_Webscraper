#include <iostream>
#include <vector>
#include <string>

using namespace std;

int numFlips(string &pancakes, int len);

int main()
{
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; test++) {
    string pancakes; // want to get to all '+'
    int len;
    cin >> pancakes >> len;
    int result = numFlips(pancakes, len);
    cout << "Case #" << test << ": ";
    if (result >= 0)
      cout << result << '\n';
    else
      cout << "IMPOSSIBLE" << '\n';
    // cout << pancakes << '\n' << len << '\n';
  }
  return 0;
}

int numFlips(string &pancakes, int len)
{
  int num_flips = 0;
  if (len == 0)
    return ((pancakes.find('-') == string::npos) ? 0 : -1);
  for (int i = 0; i < pancakes.size() + 1 - len; i++)
    if (pancakes[i] == '-') {
      num_flips++;
      for (int j = i; j < i + len; j++)
	pancakes[j] = ((pancakes[j] == '+') ? '-' : '+');
    }
  return ((pancakes.find('-') == string::npos) ? num_flips : -1);
}

