#include <iostream>
#include <string>

using namespace std;

void solve(int i, int smax, string saudience) {
  int friends = 0, new_friends;
  int standing = 0;
  for (int level = 0; level <= smax; ++level) {
    new_friends = (standing < level) ? (level - standing) : 0;
    standing += (saudience[level] - '0') + new_friends;
    friends += new_friends;
  }
  cout << "Case #" << i << ": " << friends << endl;
}

int main()
{
  int t, smax;
  string saudience;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cin >> smax >> saudience;
    solve(i + 1, smax, saudience);
  }

  return 0;
}

