#include <string>
#include <vector>
#include <iostream>
#include <map>

using std::cin;
using std::cout;
using std::endl;
using std::string;

char pancake_side(const char &pancake, int current_flips) {

  if (current_flips % 2 == 0)
  {
    return pancake;
  } else {
    return (pancake == '-') ? '+' : '-';
  }
}

int last_pancake_index(const string &pancakes, int &flips, int current_pancake) {
  int index = -1;
  for (int i = current_pancake; i > -1 ; --i)
  {
    if (pancake_side(pancakes[current_pancake], flips) == '-')
    {
      index = current_pancake;
    }
    else if (pancakes[current_pancake] == '+')
    {
      break;
    }
  }
  return index;
}

int flip_pancakes(string &pancakes) {
  int flips = 0;

  int next_index = 0;

  for (int last_pancake = pancakes.size() - 1; last_pancake > -1; --last_pancake)
  {

    next_index = last_pancake_index(pancakes, flips, last_pancake);
    if (next_index != -1)
    {
      if (pancake_side(pancakes[last_pancake], flips) == '-')
      {
        flips++;
      }
    }

  }

  return flips;
}

int main() {
  int T = 0;
  cin >> T;

  string pancakes = "";
  for (int i = 0; i < T; ++i)
  {
    cin >> pancakes;
    cout <<  "Case #" << i + 1 << ": " << flip_pancakes(pancakes) << endl;
  }


  return 0;
}
