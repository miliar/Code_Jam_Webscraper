#include <iostream>
#include <cstdio>

#include <vector>
#include <ctime>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

#define X first
#define Y second

long long gcd(long long x, long long y) {
  if(y == 0) return 1;
  while((x%=y)&&(y%=x));
  return x + y;
}

long long x, y;
void solve() {
  long long g = gcd(x, y);
  x /= g;
  y /= g;
  
  for(long long i = 1; i <= 2ll * y; i *= 2) {
    if(i == y) break;
    if(i > y) {
      cout << "impossible" << endl;
      return;
    }      
  }
  
  for(int i = 0; i < 40; i++) { 
    if(x >= y) 
      {cout << i << endl; return;}
    y /= 2;
  }
  cout << "impossible" << endl;  
  
}

int main() {
  #ifdef TVISKARON  
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
  #endif



  int t;
  cin >> t;
  for(int G = 1; G <= t; G++) {
    char t;
    cin >> x >> t >> y;
    cout << "Case #" << G << ": "; 
    solve();
  }
}