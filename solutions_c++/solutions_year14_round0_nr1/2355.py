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
  int a[16], b[16];
  int ax, bx;
  int ti;  si(ti);
  int resi[4];
  f (t, 1, ti + 1) {
    si(ax);
    fr (i, 16) {
      si(a[i]);
    }
    si(bx);
    fr (i, 16) {
      si(b[i]);
    }

    sort(a + ((ax - 1)  * 4), a + (ax * 4));
    sort(b + ((bx - 1) * 4), b + (bx * 4));
    int *res = set_intersection(a + ((ax - 1) * 4), a + (ax * 4), b + ((bx - 1) * 4), b + (bx * 4), resi);
    int cntx = (int) (res - resi);
    
    cout << "Case #" << t <<": ";
    if (cntx == 0) {
      cout << "Volunteer cheated!" << endl;
    } else if (cntx == 1) {
      cout << resi[0] << endl;
    } else {
      cout << "Bad magician!" << endl;
    }

  }
}
