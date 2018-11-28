/* 
Google codejam template
Author: Michael Yitayew
Email: myitayew@princeton.edu
LANG: C++
*/

#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath> 
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <unordered_map>

using namespace std;

int main() {

  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    string s; cin >> s;
    int count = 0;
    char prev = '-';
    if (s[0] == '-') count++;
    else prev = '+';
    int i = 1;
    while (i < s.length()) {
      if (s[i] == prev) i++;
      else if (prev == '+') { count++;
	count++;
	prev = s[i];
	i++;
      }     
      else {
	prev = s[i];
	i++;
      } 
    }
    cout<<"Case #"<<t<<": "<<count<<endl;
  }

  return 0;
}


