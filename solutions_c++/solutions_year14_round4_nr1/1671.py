#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> MI;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> MII;
typedef long long ll;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
#define X first
#define Y second

const int inf = 1e9;
const double eps = 1e-9;

int main() {
  ios_base::sync_with_stdio(false);
  int T; cin >> T;
  int ncase = 0;
  while (T--) {
    int n, x;
    cin >> n >> x;
    
    VI v(n);
    for (int i = 0; i < n; ++i)
      cin >> v[i];
    
    sort(v.rbegin(), v.rend());
    
    VI files(n,0);
    VI qtt(n, 0);
    int i = 0, act = 0, first = 0, last = n-1;
    while (i <= last) {
      if (files[act]+v[i] > x or qtt[act] == 2) ++act;
      files[act] += v[i];
      qtt[act]++;
      ++i;
      
      while (first <= act and last > i) {
        if (qtt[first] < 2 and files[first]+v[last] <= x) {
          qtt[first]++;
          files[first] += v[last];
          --last;
        }
        ++first;
      }
    }
    cout << "Case #" << ++ncase << ": " << act+1 << endl;
    
  }
 
}