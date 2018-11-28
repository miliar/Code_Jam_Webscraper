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

set<int> digits(int n){
  set<int> s;
  while(n > 0){
    s.insert(n % 10);
    n /= 10;
  }
  return s;
}

int main(void){
  int t, n;
  cin >> t;
  for(int k = 0; k < t; ++k){
    cin >> n;

    cout << "Case #" << k+1 << ": ";
    if(n == 0)
      cout << "INSOMNIA" << endl;
    else {
      int m = n;
      set<int> s = digits(n), p;
      while(s.size() < 10) {
        m += n;
        p = digits(m);
        s.insert(p.begin(), p.end());
      }
      cout << m << endl;
    }
  }

  return 0;
}
