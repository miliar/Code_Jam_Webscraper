#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm> 
#include <set>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int convert(string input)
{
  reverse(input.begin(), input.end());
  int size = input.size();
  vector<int> v;

  for (auto x : input)
  {
    if (x == '+')
    {
      v.push_back(1);
    }
    else
    {
      v.push_back(0);
    }
  }

  int count = 0;
  for (int j=0; j < size; ++j)
  {
    if (v[j] == 0)
    {
      count++;
      for (int p = j; p < size; ++p)
      {
        if (v[p] == 0)
          v[p] = 1;
        else
          v[p] = 0;
      }
    }
  }

  return count;
}

int main() 
{ 
  int t, n, m;
  string s;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << "Number of test cases : " << t << endl;

  for (int i = 1; i <= t; ++i) 
  {
    cin >> s;  // read n and then m.
    cout << "Case #" << i << ": " << convert(s) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }


  return 0;
}

