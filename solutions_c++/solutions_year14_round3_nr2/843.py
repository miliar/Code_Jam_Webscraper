#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

const long long prime = 1000000007;

bool check(string &s)
{
  vector<char> vis(30);
  char last = s[0];
  vis[last - 'a'] = true;
  for (int i = 1; i < s.size(); ++i) {
    if (s[i] != last && vis[s[i] - 'a']) return false;
    vis[s[i] - 'a'] = true;
    last = s[i];
  }
  return true;
}

long long solve(vector<string> &cars)
{
  vector<int> perm;
  for (int i = 0; i < cars.size(); ++i) perm.push_back(i); 
  long long res = 0;
  do {
    stringstream ss;
    for (int i = 0; i < perm.size(); ++i)
      ss << cars[perm[i]];
    string s = ss.str();
    if (check(s))
      res++;
  } while (next_permutation(perm.begin(),perm.end()));
  return res % prime;
}

int main()
{
  int T; cin >> T;
  vector<vector<string>> inputs;
  for (int t = 1; t <= T; ++t) {
    int N; cin >> N;
    vector<string> cars;
    for (int n = 0; n < N; ++n) {
      string car; cin >> car;
      cars.push_back(car);
    }
    cout << "Case #" << t << ": " << solve(cars) << endl;
  }
  return 0;
}
