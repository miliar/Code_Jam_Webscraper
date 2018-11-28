/*
* Author: Troy
* Date:   2015-04-11 14:08:10
* File:   main.cpp
* Last Modified time: 2015-04-11 14:39:54
*/

#include <iostream>
#include <cstdio>
#include <array>

// Problem: What is the minimum number of friends that you
// need to invite to guarantee a standing ovation?

#define MAX_PEOPLE 1000
std::array<int, MAX_PEOPLE> _arr;


void solve_case(int k)
{
  using namespace std;
  cout << "Case #" << k << ": ";

  int s_max;
  cin >> s_max;
  cin.get();

  for (int i = 0; i <= s_max; ++i)
    _arr[i] = cin.get() - '0';
  cin.get(); // eat up '\n'

  int friends_added = 0;
  int total = 0;
  for (int i = 0; i <= s_max; ++i)
  {
    total += _arr[i];
    while (total + friends_added <= i)
    {
      ++friends_added;
    }
  }
  cout << friends_added;

  cout << endl;
}

/* ------------------------- main() function ------------------------- */

int main(int argc, char const *argv[])
{
  using namespace std;
  if (argc < 2)
  {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
  }
  else
  {
    freopen(argv[1], "r", stdin);
    string output_file(argv[1]);
    output_file.append("-result.txt");
    freopen(output_file.c_str(), "w", stdout);
  }
  int case_n = 0;

  int T = 0;
  cin >> T; cin.get();

  do { solve_case(++case_n); }
  while (--T);
}
