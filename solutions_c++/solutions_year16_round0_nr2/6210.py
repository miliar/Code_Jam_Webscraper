#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <string.h>

using namespace std;

int main()
{
  unsigned int T;
  cin >> T;

  vector<string> pancakes;
  for (int i = 0; i < T; ++i)
  {
    string s;
    cin >> s;
    pancakes.push_back(s);
  }

  for (int i = 0; i < T; ++i)
  {
    int count = 0;
    string stack = pancakes[i];
    char currentStack = stack[0];
    for (int i = 0; i < stack.size(); ++i)
    {
      if (stack[i] != currentStack) {
        count ++;
        currentStack = stack[i];
      }
    }
    if (currentStack == '+') {
        //count--;
    } else {
        count ++;
    }
    cout << "Case #" << i+1 << ": " << count << endl;
  }
  return 0;
}
