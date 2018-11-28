/**
* I love coding
* @Author: Jecvay
*/

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

#define DBG 1
#define ast(b) if(DBG && !(b)) { printf("%d!!|n", __LINE__); system("pause"); }
#define dout DBG && cout << __LINE__ << ">>| "


inline int gint() {int n;scanf("%d", &n);return n;}
inline char gchar() {char c;scanf("%c", &c);return c;}
//////////////////

#define inf 0x4F4F4F4F
typedef priority_queue<pair<int, int> > Q;
const int maxn = 1e5 + 10;

int n, m;
int data[2000];

/////////////////

void printQ(Q q) {
    while(!q.empty()) {
        printf("%d ", q.top());
        q.pop();
    }
    printf("\n");
}

int f(Q q) {
 // printf("[%d]", q.size());
  pair<int, int> x = q.top();
  q.pop();

  if (x.second >= x.first)
    return x.first;

  if (x.first <= 3)
    return x.first;

  int ret = x.first;
  Q qq = q;
  for (int i = 1; i <= (x.first+1)/2; i++) {
    Q q2;
    q = qq;
    int xa = x.first - i;
    int xb = i;
    int cnt = x.second;
    bool taga = true, tagb = true;
    if (q.empty()) {
      if (xa == xb) {
        q2.push(make_pair(xa, cnt * 2));
      } else {
        if (xa) q2.push(make_pair(xa, cnt));
        if (xb) q2.push(make_pair(xb, cnt));
      }
    } else {
      taga = tagb = false;
    }
    while (!q.empty()) {
      if (xa == xb) {
        if (q.top().first == xa) {
          q2.push(make_pair(xa, q.top().second + cnt * 2));
          taga = tagb = true;
        } else {
          q2.push(q.top());
        }
      } else {
        if (q.top().first == xa) {
          q2.push(make_pair(xa, q.top().second + cnt));
          taga = true;
        } else if (q.top().first == xb) {
          q2.push(make_pair(xb, q.top().second + cnt));
          tagb = true;
        } else {
          q2.push(q.top());
        }
      }
      q.pop();
    }
    if (xa != xb) {
      if (!taga) q2.push(make_pair(xa, cnt));
      if (!tagb) q2.push(make_pair(xb, cnt));
    } else {
      if (!taga) q2.push(make_pair(xa, cnt * 2));
    }

    // printQ(q2);
    ret =  min(ret, x.second + f(q2));
  }
  return ret;
}




int main() {
  int t = gint();
  for (int cas = 1; cas <= t; cas++) {
    n = gint();
    memset(data, 0, sizeof(data));
    Q q;
    for (int i = 0; i < n; i++) {
      data[gint()]++;
    }
    for (int i = 1; i < 1001; i++) {
      if (data[i]) {
        q.push(make_pair(i, data[i]));
      }
    }
    printf("Case #%d: %d\n", cas, f(q));
  }
  return 0;
}



/*

1
3
8 2 6

*/
