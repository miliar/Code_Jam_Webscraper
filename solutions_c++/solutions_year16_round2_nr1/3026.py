/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int ch[10][26];

string f(string s) {
  string digits[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

  vi f(26, 0);

  for(int i=0; i < s.size(); i++) {
    f[s[i] - 'A'] ++;
    //cout << (s[i] - 'A') << endl;
  }
  vi ans(9,0);
  ans[0] = f['Z' - 'A'];
  ans[2] = f['W' - 'A'];
  ans[6] = f['X' - 'A'];
  ans[7] = f['S' - 'A'] - ans[6];
  ans[5] = f['V' - 'A'] - ans[7];
  ans[4] = f['U' - 'A'];
  ans[3] = f['R' - 'A'] - ans[0] - ans[4];
  ans[1] = f['O' - 'A'] - ans[0] - ans[2] - ans[4];
  ans[8] = f['G' - 'A'];
  ans[9] = f['I' - 'A'] - ans[8] - ans[6] - ans[5]; 
   
  string r;
  for(int i=0;i<=9;i++) {
    for(int j=0;j<ans[i];j++) {
      r += '0' + i;
    }
  }
  return r;
}

int main(){
  assert(f("WEIGHFOXTOURIST") == "2468");
  int T;
  cin >> T;
  for (int i=1;i<=T;i++) {
    string s;
    cin >> s;
    printf("Case #%d: %s\n", i, f(s).c_str());
  }
}






