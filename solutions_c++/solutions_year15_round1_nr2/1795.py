#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#include <cstring>
#include <cstddef>

using namespace std;

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
    c = a; a = b%a;  b = c;
  }
  return b;
}

int lca(int a, int b){
  return a / gcd(a, b) * b;
}

int a[1003];

int main(){
  FILE *fin = freopen("B-small.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("B-small.ans", "w", stdout);
  int T;
  cin >> T;

  for(int t = 1; t <= T; t++){
    int b, n;
    cin >> b >> n;
    long long cnt = 1;
    for(int i = 1; i <= b; i++){
      cin >> a[i];
      cnt = lca(cnt, a[i]);
    }

    int j = 0;
    bool ok = false;
    for(int x = 0; !ok && x < cnt; x++){
      for(int i = 1; !ok && i <= b; i++){
        /* cout << "x = " << x  << "ai = " << a[i] << endl; */
        if(x % a[i] == 0){
          j++;
          if(j == n){
            cout << "Case #" << t << ": " << i << endl;
            ok = true;
          }
        }
      }
    }
    if(!ok){
      n %= j;
      if(n == 0)
        n = j;
    j = 0;
    for(int x = 0; !ok && x < cnt; x++){
      for(int i = 1; !ok && i <= b; i++){
        /* cout << "x = " << x  << "ai = " << a[i] << endl; */
        if(x % a[i] == 0){
          j++;
          if(j == n){
            cout << "Case #" << t << ": " << i << endl;
            ok = true;
          }
        }
      }
    }
    }
}
}

