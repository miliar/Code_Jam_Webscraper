/**
 * Problem: D
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <math.h>
#include <set>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <assert.h>
#include <map>

#include <sstream>

#include <stdexcept>

using namespace std;

typedef vector<string> vs;
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<ll> vll;


int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  string str;
  string tmp;
  for (int caseI = 1; caseI <= cases; caseI++) {
    cin >> str;
    tmp = str[0];
    for (int i = 1; i < str.size(); i++) {
      if (str[i] < tmp[0]) {
        tmp += str[i];
      } else {
        tmp = str[i] + tmp;
      }
    }
    cout << "Case #" << caseI << ": " << tmp << endl;
  }
  return 0;
}
