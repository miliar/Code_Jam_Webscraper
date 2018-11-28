#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <string>
#include <climits>
#include <stack>
#include <queue>
using namespace std;

#define LL long long
#define MP make_pair
#define PB push_back
#define PP pop_back
#define FO(a) freopen(a, "r", stdin)

const int MAX = INT_MAX;
const long long LMAX = LONG_MAX;
const int MIN = INT_MIN;
const long long LMIN = LONG_MIN;

int main() {
  //FO("./A-large.in");
  int T;
  int C = 1;
  cin >> T;
  while(C <= T) {
    int len;
    cin >> len;
    string str;
    cin >> str;
    int * arr = new int[len+2];
    int * table = new int[len+2];

    for(int i = 0; i < len+1; i ++) {
      arr[i] = str[i] - '0';
    }

    table[0] = arr[0];

    int ret = 0;
    for(int i = 1; i <= len; i ++) {
      int delta = 0;
      if(arr[i] > 0) {
        ret += max(0, (i - table[i-1]));
        delta += max(0, (i - table[i-1]));
      }
      table[i] = table[i-1] + arr[i] + delta;
    }

    delete [] arr;
    delete [] table;
    cout << "Case #" << C << ": " << ret << endl;
    C ++;
  }
}
