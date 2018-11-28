// written by lonerdude(dvdreddy)
// all rights reserved
//the template by dvdreddy
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sf(x) scanf("%lf",&x)
#define ss(x) scanf("%s",&x)

#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,n)  f(i,0,n)

typedef long long ll;

int a[1002];

bool check(int xi){
  int dig[1000];
  int x = xi; int cnt = 0;
  while (x){
    dig[cnt] = x % 10;
    x /= 10; cnt++;
  }
  fr (i, cnt){
    if (dig[i] != dig[cnt - i - 1]){
      return false;
    }
  }

  int px = (int)sqrt(xi);
  if (px * px != xi){
    return false;
  }
  cnt = 0;
  while (px){
    dig[cnt] = px % 10; px /= 10; cnt++;
  }
  fr (i, cnt){
    if (dig[i] != dig[cnt - i - 1]){
      return false;
    }
  }
  return true;
}


int main(){
  int t;
  si(t);
  a[0] = 0;
  f (i, 1, 1002){
    a[i] = check(i);
  }
  f (i, 1, 1002){
    a[i] += a[i - 1];
  }
  int cnt = 1;
  while (t--){
    int ax; int bx;
    cin >> ax >> bx;
    cout << "Case #" << cnt << ": " <<a[bx] - a[ax - 1] << endl;
    cnt++;
  }
  return 0;
}
