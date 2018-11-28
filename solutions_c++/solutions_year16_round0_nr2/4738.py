#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string::iterator> find_flip_points(string & s)
{
  bool first = false;

  vector<string::iterator> ret(2);

  for (string::iterator i = s.begin(); i != s.end(); ++i)
  {
    if (*i == '-')
    {
      first = true;

      string::iterator j = 1 + i;
      while (j != s.end() && *j == '-') ++j;

      ret[0] = i;
      ret[1] = j;

      break;
    }
  }

  if (!first)
  {
    cerr << "unexpected state: no `-` found!" << endl;
    exit(-1);
  }

  return ret;
}

void flip_pancake(string::iterator begin, string::iterator end)
{
  for (string::iterator i = begin; i != end; ++i)
  {
    if (*i == '+') *i = '-';
    else *i = '+';
  }
}

bool valid(string &s)
{
  for (int i = 0; i < (int) s.length(); ++i)
    if (s[i] == '-') return false;

  // cerr << s << " is valid" << endl;
  return true;
}

int solve(string &st)
{
  int ret = 0;

  while (!valid(st))
  {
    // cerr << "checking: " << st << endl;

    vector<string::iterator> flip = find_flip_points(st);

    // cerr << "flipping " << (flip[0] - st.begin()) << " to " << (flip[1] - st.begin()) << endl;
    flip_pancake(st.begin(), flip[1]);

    ++ret;
  }

  return ret;
}

int main(int argc, char ** argv)
{
  int tests; cin >> tests;

  for (int tc = 0; tc < tests; ++tc)
  {
    string st; cin >> st;

    int rc = solve(st);

    cout << "Case #" << (1 + tc) << ": " << rc << endl;
    // cerr << "pancakes are: " << st << endl;
  }

  return 0;
}
