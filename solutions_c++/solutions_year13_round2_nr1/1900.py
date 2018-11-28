#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <bitset>
#include <utility>
#include <limits>
#include <iterator>
#include <numeric>

using namespace std;

int main(int argc, char** argv){

  unsigned long T;
  cin >> T;

  for(unsigned long t=1; t<=T; ++t){

    long my_size;
    cin >> my_size;
    long count;
    cin >> count;

    vector<long> motes;
    for (long i = 0; i < count; i++)
    {
      long temp;
      cin >> temp;
      motes.push_back(temp);
    }

    sort(motes.begin(), motes.end());

    long steps = 0;
    long rest = motes.size();
    long min_steps = motes.size();
    for (int i = 0; i < motes.size(); i++)
    {
      if (my_size <= 1)
      {
        steps = min_steps;
        break;
      }

      if (steps + rest < min_steps)
      {
        min_steps = steps + rest;
      }

      while (my_size <= motes[i])
      {
        steps++;
        my_size += (my_size - 1);
      }

      my_size += motes[i];

      rest--;
    }

    if (steps < min_steps) min_steps = steps;

    cout << "Case #" << t << ": " << min_steps;

    cout << endl;
  }

  return 0;
}
