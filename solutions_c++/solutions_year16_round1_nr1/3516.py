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
#include <list>

#define PI 3.14159265

using namespace std;

bool should_push_front(list<char> l, char c)
{
  bool res;
  std::list<char>::iterator it = l.begin();
  if (c > *it)
    return true;
  if (c < *it)
    return false;
  while ((it != l.end()) && (c == *it))
  {
    c = *it;
    advance(it,1);
  }
  if (c > *it)
    return true;
  return false;
}


int main(int argc, const char *argv[])
{
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i)
  {
    string s;
    cin >> s;
    list <char> l1;
    l1.push_back(s[0]);
    for (int j = 1; j < s.size(); ++j)
    {
      if (should_push_front(l1, s[j]))
        l1.push_front(s[j]);
      else
        l1.push_back(s[j]);
    }
    cout << "CASE #" << i+1 << ": ";
    for (list<char>::iterator it = l1.begin(); it != l1.end(); advance(it, 1))
      cout << *it;
    cout << endl;
  }
  return 0;
}


