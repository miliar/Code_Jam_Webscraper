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

#define MOD 1000000007

typedef vector<string> vs;
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<ll> vll;

int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  int N, total, k, j;
  string str;
  int array[1005];
  for(int caseI = 1; caseI <= cases; caseI++) {
    total = 0, k = 0;
    cin >> N >> str;
    for(int i=0; i<=N; i++) {
      array[i] = str[i] - 48;
    }
    j = 0;
    while(j<=N) {
      if(total < j) {
        k += j - total;
        total += j - total;
      }
      total += array[j];
      j++;
    }

    cout << "Case #" << caseI << ": " << k << endl;
  }

  return 0;
}
