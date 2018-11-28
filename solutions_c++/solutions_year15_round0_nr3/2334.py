#include <cstdio>
#include <cmath>
#include <algorithm>
#define MAXL 10005

using namespace std;

int l;
long long x;
char str[MAXL];
int prefix[MAXL];

// 1 = 1
// i = 2
// j = 3
// k = 4

int mult(int a, int b) {
  if(abs(a) == 1 || abs(b) == 1)
    return a * b;
  bool neg = a*b < 0;
  a = abs(a);
  b = abs(b);
  int raw;
  bool rev = false;
  if(a == b) {
    raw = -1;
  } else {
    rev = a > b;
    if(rev) {
      swap(a, b);
    }
    if(a+1 == b) {
      raw = a == 2 ? 4 : 2;
    } else {
      raw = -3;
    }
  }
  return raw * (neg ? -1 : 1) * (rev ? -1 : 1);
}

//b * ? = a
int prediv(int a, int b) {
  bool neg = a * b < 0;
  a = abs(a);
  b = abs(b);
  int raw;
  if(a == 1) {
    switch(b) {
    case 1:
      raw = 1;
      break;
    case 2:
      raw = -2;
      break;
    case 3:
      raw = -3;
      break;
    case 4:
      raw = -4;
      break;
    }
  } else if(a == 2) {
      switch(b) {
    case 1:
      raw = 2;
      break;
    case 2:
      raw = 1;
      break;
    case 3:
      raw = 4;
      break;
    case 4:
      raw = -3;
      break;
    }
  } else if(a == 3) {
      switch(b) {
    case 1:
      raw = 3;
      break;
    case 2:
      raw = -4;
      break;
    case 3:
      raw = 1;
      break;
    case 4:
      raw = 2;
      break;
    }
  } else {
      switch(b) {
    case 1:
      raw = 4;
      break;
    case 2:
      raw = 3;
      break;
    case 3:
      raw = -2;
      break;
    case 4:
      raw = 1;
      break;
    }
  }
  return raw * (neg ? -1 : 1);
}

int num(char c) {
  return 2 + (c - 'i');
}

int pow2(int x, long long p) {
  if(x == 1)
    return 1;
  if(x == -1)
    return p % 2 == 1 ? -1 : 1;
  if(p % 2 == 0) {
    return p % 4 == 0 ? 1 : -1;
  } else {
    return (p-1) % 4 == 0 ? x : -x;
  }
}

int calc(long long n) {
  int res = prefix[n % l + 1];
  if(n >= l) {
    long long cnt = n / l;
    res = mult(pow2(prefix[l], cnt), res);
  }
  return res;
}

int main() {
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%d %lld\n", &l, &x);
    scanf("%s", str);

    prefix[0] = 1;

    for(int i = 0; i < l; i++) {
      prefix[i+1] = mult(prefix[i], num(str[i]));
    }

    bool ok = true;
    if(x % 2 == 1) {
      if(prefix[l] != -1) {
        ok = false;
      }
    } else {
      if(prefix[l] == 1 || prefix[l] == -1) {
	ok = false;
      } else {
	if(x % 4 == 0)
	  ok = false;
      }
    }

    if(!ok) {
      printf("Case #%d: NO\n", kase);
      continue;
    }

    long long ii = -1;
    for(long long i = 0; i < l*x; i++) {
      if(calc(i) == 2) {
	ii = i;
	break;
      }
    }

    if(ii == -1) {
      printf("Case #%d: NO\n", kase);
      continue;
    }
    
    long long kk = -1;
    for(long long i = l*x - 1; i > 0; i--) {
      if(prediv(-1, calc(i - 1)) == 4) {
	kk = i;
	break;
      }
    }
    
    if(kk == -1) {
      printf("Case #%d: NO\n", kase);
      continue;
    }
    
    if(kk > ii+1) {
      printf("Case #%d: YES\n", kase);
    } else {
      printf("Case #%d: NO\n", kase);
    }

  }
  return 0;
}
