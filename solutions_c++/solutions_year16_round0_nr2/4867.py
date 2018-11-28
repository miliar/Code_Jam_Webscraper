#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

typedef long long ll;

int main(void){
  int t;
  string s;
  cin >> t;
  for(int k = 0; k < t; ++k){
    cin >> s;

    int flip = 0, last = s.size() - 1;
    while(last > 0 && s[last] == '+')
      --last;
    while(s[last] == '-') {
      if(last > 0 && s[0] == '+') {
        int p = 0;
        while(p < last && s[p] == '+') {
          s[p] = '-';
          ++p;
        }
        ++flip;
      }
      for(int i = 0; i <= last; ++i)
        s[i] = s[i] == '+' ? '-' : '+';
      reverse(s.begin(), s.begin()+last+1);
      ++flip;
      while(last > 0 && s[last] == '+')
        --last;
    }

    cout << "Case #" << k+1 << ": " << flip << endl;
  }

  return 0;
}
