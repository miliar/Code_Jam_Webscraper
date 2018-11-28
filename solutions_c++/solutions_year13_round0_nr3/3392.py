#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;
const int ten[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
int pick(ll x, int k) {
  return x / ten[k] % 10;
}
int cntlen(ll x) {
  int ret = 0;
  while(x) ret ++, x/=10;
  return ret;
}
int isPalim(ll x) {
  int len = cntlen(x);
  for(int i = 0; i < len / 2; ++ i) {
    if (pick(x , i) != pick(x, len - 1 - i)) {
      return 0;
    }
  }
  return 1;
}
ll getSqrt(ll x, int d) {
  ll ret = (int)sqrt(x);
  if (ret * ret != x) {
    ret += d;
  }
  return ret;
}

int pre[8][10000 + 10];
void init() {
  for(int i = 1; i < 10000; ++ i) {
    int len = cntlen(i);
    // for palindrome bit cnt is odd

    int key = i / 10;
    for(int j = 0; j < len; ++ j) {
      key = key * 10 + pick(i, j);
    }
    pre[len * 2 - 1][i] = isPalim(key * 1LL * key);
    if (len == 4) continue;


    // for palindrome bit cnt is even
    key = i;
    for(int j = 0; j < len; ++ j) {
      key = key * 10 + pick(i, j);
    }
    pre[len * 2][i] = isPalim(key * 1LL * key);
  }

  for(int i = 0; i < 8; ++ i) {
    for(int j = 2; j <= 10000; j ++) {
      pre[i][j] += pre[i][j - 1];
    }
  }
}

int main()
{
#ifdef _ZZZ_
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
#endif
  init();
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; ++ tt) {
    ll L, R;
    cin >> L >> R;
    ll l = getSqrt(L, 1), r = getSqrt(R, 0);
    int lenl = cntlen(l), lenr = cntlen(r);
    int len_start = lenl, len_end = lenr;
    int ans = 0;
    //cout << "haha " << l << " " << r << endl;

    if (len_start < len_end) {

      // for start
      if (1) {
        ll tmp = l / ten[lenl / 2];
        ll tmppmt = tmp;
        for(int i = 0; i < lenl / 2; ++ i) {
          tmppmt = tmppmt * 10 + pick(tmp, i);
        }
        if (tmppmt < l) {
          tmp ++;
        }

        ans += pre[len_start][10000] - pre[len_start][tmp - 1];
        //cout << "start: " << tmp << " ans = " << ans << endl;
        ++ len_start;
      }

      // for end
      if (1) {
        ll tmp = r / ten[lenr / 2];
        //cout << "end0: " << tmp << " " << r << endl;
        ll tmppmt = tmp;
        for(int i = 0; i < lenr / 2; ++ i) {
          tmppmt = tmppmt * 10 + pick(tmp, i);
        }
        if (tmppmt > r) {
          tmp --;
        }

        ans += pre[len_end][tmp] - pre[len_end][0];
       // cout << "end: " << tmp << " " << len_end << " ans = " << ans << endl;
        -- len_end;
      }
      for(int ilen = len_start; ilen <= len_end; ++ ilen) {
        ans += pre[ilen][10000];
      }
    } else {
        ll tmp1 = l / ten[lenl / 2];
        ll tmppmt = tmp1;
        for(int i = 0; i < lenl / 2; ++ i) {
          tmppmt = tmppmt * 10 + pick(tmp1, i);
        }
        if (tmppmt < l) {
          tmp1 ++;
        }
        ll tmp2 = r / ten[lenr / 2];
        tmppmt = tmp2;
        for(int i = 0; i < lenr / 2; ++ i) {
          tmppmt = tmppmt * 10 + pick(tmp2, i);
        }
        if (tmppmt > r) {
          tmp2 --;
        }
        ans = pre[len_start][tmp2] - pre[len_start][tmp1 - 1];
    }


    cout << "Case #" << tt << ": " << ans << endl;

  }
  return 0;
}










