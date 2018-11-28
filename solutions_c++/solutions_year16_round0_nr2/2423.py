#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>
#include <cstring>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

string s;
int n;
int B[101][101][2];

int best(int a, int b, int k) {
  if (b < a)
    return 0;
  int &sol = B[a][b][k];
  if (sol != -1)
    return sol;
  if (k == 0 && s[b] == '+')
    return sol = best(a, b-1, k);
  if (k == 1 && s[b] == '-')
    return sol = best(a, b-1, k);
  sol = best(a, b-1, 1-k)+1;
  return sol;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    cout << "Case #" << tt+1 << ": ";
    cin >> s;
    n = (int)s.size();
    memset(B, -1, sizeof B);
    cout << best(0, n-1, 0) << endl;
  }
  return 0;
}
