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

ll maxi = 1000000007;

int main() {
  int ti;
  si(ti);
  ll ax[1000];
  f (t, 1, ti + 1) {
    int nx;
    si(nx);
    fr (i, nx) {
      sll(ax[i]);
    }
    ll res_max = 0;
    int i = 0; int j = nx;
    while (i < j) {
      
      ll mini = maxi;
      int pos = -1;
      f (k, i, j) {
        mini = min(ax[k], mini);
        if (mini == ax[k]) {
          pos = k;
        }
      }
      
      if (pos == -1) {
        cout << "dsssss " << endl;
      }
      
      // cout << "xxx " << i << " " << j << " " << pos << endl;
      
      if ((j - 1 - pos) < (pos - i)) {
        f (k, pos + 1, j) {
          ax[k - 1] = ax[k];
        }
        ax[j - 1] = mini;
        res_max += (j - 1 - pos);
        j--;

        // cout << " sss " << res_max << " " << (j - 1 - pos) << endl;
      } else {
        f (k, i, pos) {
          ax[pos - (k - i)] = ax[pos - (k - i) - 1];
        }
        ax[i] = mini;
        res_max += (pos - i);
        i++;
      }             
    }

    
    cout << "Case #" << t << ": " << res_max << endl;
  }

  return 0;
}
