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
#include <set>

using namespace std;

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sf(x) scanf("%lf",&x)
#define ss(x) scanf("%s",&x)

#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,n)  f(i,0,n)

typedef long long ll;


int main() {
  double d_girl[10000];
  double d_boy[10000];
  int ti;
  si(ti);
  f (t, 1, ti + 1) {
    int n;
    si(n);
    fr (i, n) {
      cin >> d_girl[i];
    }
    sort(d_girl, d_girl + n);
    fr (i, n) {
      cin >> d_boy[i];
    }
    sort(d_boy, d_boy + n);

    int cheat_count = 0;
    int count = 0;
    
    // computation for cheat_count
    int st_girl = 0; // start of girl
    int st_boy = 0; // start of boy
    // loop on the number of elements in the array
    for (int i = n; i > 0; i--) {
      if (d_girl[st_girl] > d_boy[st_boy]) {
        cheat_count++;
        st_girl++; st_boy++;
      } else {
        st_girl++;
      }      
    }
    
    // computation for count
    set<double> boy_set (d_boy, d_boy + n);
    for (int i = 0; i < n; i++) {
      set<double>::iterator it;
      it = boy_set.upper_bound(d_girl[i]);
      if (it == boy_set.end()) {
        boy_set.erase(boy_set.begin());
        count++;
      } else {
        boy_set.erase(it);
      }
    }
    cout << "Case #" << t << ": " << cheat_count << " " << count << endl;
  }

}
