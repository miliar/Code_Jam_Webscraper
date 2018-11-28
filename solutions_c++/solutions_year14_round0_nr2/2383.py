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


int main() {
  int ti;
  si(ti);
  f (t, 1, ti + 1) {
    double c, f, x;
    cin >> c >> f >> x;
    double res = 0;;
    double cur_rate = 2.0;
    while (true) {
      if ((c / cur_rate) + (x / (f + cur_rate)) < (x / cur_rate)) {
        res += (c / cur_rate); cur_rate += f;
      } else {
        res += (x / cur_rate); break;
      }
    }   
    printf("Case #%d: %.9f", t, res);
    cout << endl;
  }

}
