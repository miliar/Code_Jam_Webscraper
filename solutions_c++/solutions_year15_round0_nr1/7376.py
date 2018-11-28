#include <cstdio>
#include <climits>
#include <cinttypes>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <algorithm>

using namespace std;

int t;

int solve(string& digits) {
  int answer = 0;
  int standings = digits[0] - '0';

  for (int i = 1; i < digits.length(); ++i) {
    if (standings < i) {
      answer += i - standings;
      standings = i + (digits[i] - '0');
    } else {
      standings += digits[i] - '0';
    }
  }

  return answer;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  scanf("%d\n", &t);
  for (int i = 0; i < t; ++i) {
    string str; 
    getline(cin, str);

    int smax;
    string digits;
    istringstream ss(str);
    ss >> smax >> digits;
    printf("Case #%d: %d\n", i + 1, solve(digits));    
  }

  return 0;
}
