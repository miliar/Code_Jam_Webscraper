#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <utility>
#include <queue>

#define PI 3.14159265

using namespace std;

char nygate(char c)
{
  if ( c == '+') return '-';
  return '+';
}

inline void apply_rotation(string& s, size_t upto)
{
  string temp;
  temp.resize(upto-1);
  for (int i = 0; i < upto; ++i)
    temp[i] = nygate(s[upto-i-1]);
  for (int i = 0; i < upto; ++i)
    s[i] = temp[i];
}

int get_moves(string& s, size_t stop)
{
  if (stop < 0) return 0;
  int it = stop;
  while ((s[it] == '+') && (it >= 0))  --it;
  // now start..it is without + suffix
  if (it < 0)
    return 0;
  // s[it] == '-';

  int moves = 0;
  int itt = 0;
  while ((s[itt] == '+') && (itt < it)) ++itt;
  // now 0..itt is longest '+' prefix we first need to repair
  if ((itt > 0) || (s[itt] == '+'))
  {
    moves++;
    if (itt == 0) s[0] = '-';
    else apply_rotation(s, itt);
  }

  while ((s[itt] == '-') && (itt < it)) itt++;
  // now s[0..itt] is longest '-' prefix
  // found biggest '-' prefix, lest invert it and now search only to
  if (it == itt) return ++moves;
  apply_rotation(s, it+1);
  moves++;
  return moves + get_moves(s, it-itt);
}

int main(int argc, const char *argv[])
{
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i)
  {
    string str;
    cin >> str;
    int nmoves = get_moves(str, str.size()-1);
    cout << "Case #" << i+1 << ": " << nmoves << endl;
  }
  return 0;
}


