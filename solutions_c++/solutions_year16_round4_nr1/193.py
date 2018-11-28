#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int N,T;
int P,R,S;
string ans[13][4];

ifstream fin("A.in");
ofstream fout("A.out");

int main() {
  fin >> T;
  ans[0][0] = "P";
  ans[0][1] = "R";
  ans[0][2] = "S";
  for (int i = 1; i <= 12; i++) {
    string test1,test2;
    test1 = ans[i-1][0]+ans[i-1][1];
    test2 = ans[i-1][1]+ans[i-1][0];
    if (test1.compare(test2) < 0) ans[i][0] = test1;
    else ans[i][0] = test2;
    test1 = ans[i-1][1]+ans[i-1][2];
    test2 = ans[i-1][2]+ans[i-1][1];
    if (test1.compare(test2) < 0) ans[i][1] = test1;
    else ans[i][1] = test2;
    test1 = ans[i-1][0]+ans[i-1][2];
    test2 = ans[i-1][2]+ans[i-1][0];
    if (test1.compare(test2) < 0) ans[i][2] = test1;
    else ans[i][2] = test2;
  }
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    fin >> N >> R >> P >> S;
    bool found = false;
    string res = "z";
    for (int i = 0; i < 3; i++) {
      string test = ans[N][i];
      int a,b,c;
      a = 0; b = 0; c = 0;
      for (int j = 0; j < test.length(); j++) {
        if (test[j] == 'R') a++;
        else if (test[j] == 'P') b++;
        else c++; 
      }
      cout << a << " " << b << " " << c << "\n";
      if (R == a && P == b && S == c) {
        if (test.compare(res) < 0) res = test;
        found = true;
      }
    }
    if (!found) fout << "Case #" << tt << ": " << "IMPOSSIBLE" << "\n";
    else fout << "Case #" << tt << ": " << res << "\n";
  }
  return 0;
}