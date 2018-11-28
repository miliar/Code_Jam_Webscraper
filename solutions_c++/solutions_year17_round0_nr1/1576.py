#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

int solve(string &s, int k) {
  int n = (int)s.size();
  int cnt = 0;
  for (int i=0; i+k-1<n; i++)
    if (s[i] == '-') {
      cnt++;
      for (int j=0; j<k; j++)
        s[i+j] = s[i+j] == '+'?'-':'+';
    }
  for (int i=0; i<n; i++)
    if (s[i] == '-')
      return -1;
  return cnt;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    string s;
    int k;
    cin >> s >> k;    
    int sol = solve(s, k);
    cout << "Case #" << tt+1 << ": ";
    if (sol == -1)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << sol << endl;
  }
  return 0;
}
