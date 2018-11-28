#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <limits>
#include <utility>
#include <iomanip>
#include <cassert>

#define endl '\n'
using namespace std;
typedef unsigned long long BI;

int k,c,s;

int main(){

  int t;
  cin >> t;
  for(int tc=1;tc<=t;tc++){
    cin >> k >> c >> s;
    BI cur = 1;
    BI diff = (BI)pow(k,c-1);
    cout << "Case #" << tc << ": ";
    for(int i=0;i<s;i++){
      cout << cur << " \n"[i == s-1];
      cur += diff;
    }
  }
  return 0;
}
