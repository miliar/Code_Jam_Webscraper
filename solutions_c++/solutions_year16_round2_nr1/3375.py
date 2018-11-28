#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-10
#define INF 1000000000
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

int main() {
  int T;
  string uniq = "ZWUXGFVTON";
  string order = "ZOWTUFXVGN";
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    string S;
    cin >> S;

    map<char, int> mp;
    mp['Z'] = 0; // 0
    mp['O'] = 0; // 1
    mp['W'] = 0; // 2
    mp['T'] = 0; // 3
    mp['U'] = 0; // 4
    mp['F'] = 0; // 5
    mp['X'] = 0; // 6
    mp['V'] = 0; // 7
    mp['G'] = 0; // 8
    mp['N'] = 0; // 9

    for (int i = 0; i < S.size(); i++) {
      mp[S[i]]++;
    }

    for (int i = 0; i < uniq.size(); i++) {
      if (i == 0) {                         //0
        mp['O'] = max(mp['O']-mp['Z'], 0);
      } else if (i == 1) {                  //2
        mp['O'] = max(mp['O']-mp['W'], 0);
        mp['T'] = max(mp['T']-mp['W'], 0);
      } else if (i == 2) {                  //4
        mp['F'] = max(mp['F']-mp['U'], 0);
        mp['O'] = max(mp['O']-mp['U'], 0);
      } else if (i == 3) {                  //6
      } else if (i == 4) {                  //8
        mp['T'] = max(mp['T']-mp['G'], 0);
      } else if (i == 5) {                  //5
        mp['V'] = max(mp['V']-mp['F'], 0);
      } else if (i == 6) {                  //7
        mp['N'] = max(mp['N']-mp['V'], 0);
      } else if (i == 7) {                  //3
      } else if (i == 8) {                  //1
        mp['N'] = max(mp['N']-mp['O'], 0);
      } else if (i == 9) {                  //9
        mp['N'] = mp['N'] / 2;
      }
    }

    cout << "Case #" << t << ": ";
    for (int i = 0; i < order.size(); i++) {
      for (int j = 0; j < mp[order[i]]; j++) {
        cout << i;
      }
    }
    cout << endl;
  }
}

