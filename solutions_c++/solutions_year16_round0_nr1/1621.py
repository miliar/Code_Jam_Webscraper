#include <iostream>
#include <set>
using namespace std;
typedef unsigned long long ull;

int main() {
  ull T, N, res, val, x, y, tc;
  bool ch[10], ins;
  set<ull> v;
  cin >> T;
  for(tc=1; tc<=T; tc++) {
    cin >> N;
    for(int i=0; i<10; i++) ch[i] = false;
    val = 0;
    v.clear();
    x = 1;
    ins = false;
    while(val != 45 || !ch[0]) {
      res = x * N;
      if(v.find(res) != v.end()) {
        ins = true;
        break;
      }
      else {
        v.insert(res);
      }
      while(res) {
        y = res % 10;
        if(!ch[y]) val += y;
        ch[y] = true;
        res /= 10;
      }
      res = x * N;
      x++;
    }
    cout << "Case #" << tc << ": ";
    if(ins) cout << "INSOMNIA" << endl;
    else cout << res << endl;
  }
  return 0;
}

