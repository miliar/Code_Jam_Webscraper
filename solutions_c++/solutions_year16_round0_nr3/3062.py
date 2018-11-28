// Tapan Sahni
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <iomanip>
#include <map>
#include <complex>
#include <set>

using namespace std;
typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e5 + 10;
const LL mod = 1000000007;

vector <int> v;

void pbin(LL val, LL len) {
  for(LL i = len - 1; i >= 0; i--) {
    if((1LL << i) & val)
      cout << "1";
    else cout <<"0";
  }
  cout << " ";
  return;
}

void solve() {
  int t, tNum = 1; 
  cin >> t;
  cout << "Case #1:";
  cout << endl;
  while(t--) {
    int val = 5;
    int n, J;
    cin >> n >> J;
    for(LL i = 0; i < (1LL << (n - 2)); i++) {
      v.clear();
      int j = 1;
      bool f = false;
      while(j <= 10) {
        if(j == 1) {
          val = 0;
          j++;
          continue;
        }
        for(int k = 2; k < 111; k++) {
          if(k > 100) 
            continue;
          LL tmp = 2 * 1LL * i + (1LL << (n - 1)) + 1;
          LL cnt = 1, add = 1;
          while(tmp > 0) {
            if(tmp & 1) 
              cnt = (cnt + add) % k;
              tmp = tmp >> 1;
              add = add * 1LL * j;
          }
          if(cnt == 1) {
            v.push_back(k);
            f = true;
            break;
          } 
        }
        j++;
      }
      int x1 = (int) v.size();
      if(x1 == 9) {
        J--;
        pbin(2 * 1LL * i + (1LL << (n - 1)) + 1, n);
        for(int i = 0; i < 9; i++) {
          cout << v[i] << " ";
        }
        cout <<"\n";
        if(J == 0)
          break;
      }
    }
    tNum++;
  }
  return; 
}
int main() {
    ios::sync_with_stdio(false) ; cin.tie(nullptr);
    solve();
    return  0;
}
// Never Quit
