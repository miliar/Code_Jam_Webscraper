#include <bits/stdc++.h>

using namespace std;
const int MAXN = 1000000;

int t;
long long n;
int digits;
bool d[10];
inline void clear();
inline bool is_ready();
inline bool mark(long long x);
long long res[MAXN + 5];

int main() {
  for(long long int i = 0; i <= MAXN; ++i) {
    clear();
    n = i;
    mark(n);
    for(int f = 0; f < 200; ++f) {
      if(!is_ready()) n += i;
      mark(n);
    }
    if(is_ready()) res[i] = n;
    else res[i] = -1;
  }

  scanf("%d", &t);
  for(int Case = 1; Case <= t; ++Case) {
    scanf("%lld", &n);
    if(res[n] > 0) printf("Case #%d: %lld\n", Case, res[n]);
    else printf("Case #%d: INSOMNIA\n", Case);
  }  
  return 0;
}

inline void clear() {
  for(int i = 0; i <= 9; ++i) {
    d[i] = false;
  }
  digits = 0;
}

inline bool is_ready() {
  return digits == 10;
}

inline bool mark(long long x) {
  bool ret = false;
  while(x > 0LL) {
    int ind = int(x % (long long)10);
    if(!d[ind]) {
      ret = true;
      ++digits;
    }
    d[ind] = true;
    x /= 10LL; 
  }
  return ret;
}
