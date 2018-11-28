#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define maxint 2147000000
int tmp = 0, n, t;
int f[5000001], mark[1000001];

int rev (int now) {
    int ans  = 0;
    //if (now % 10 == 0) return now;
    while (now) {
          ans = ans * 10 + now%10;
          now = now/10;
    }
    //cout << ans << endl;
    return ans;
}
int get (int now) {
    cout << now << endl;
    if (now <= 1000000 && f[now] > 0)
       return f[now];
    if (now < 10) {
            f[now] = now;
            return now;
    }
    int t1 = now - 1, t2 = rev (now);
    if (t1 < t2) {
       f[now] = 1 + get (t1);
       return f[now];
       }
    else {
         f[now] = 1 + get (t2);   
         return f[now];
         } 
}

int get2 (int now) {
    cout << now << endl;
    if (now > 1000000)
       return maxint;
    if (mark[now]) 
       return maxint;
    if (now < 20) return now;
    mark[now] = 1;
    int t1 = now-1, t2 = rev(now);
    if (now % 10 == 0) return 1+get2 (t1);
    else {
         return 1 + min (get2 (t1), get2 (t2));
    }    
}
void solve () {
     memset (mark, 0 ,sizeof (mark));
     cin >> n;
     cout << "Case #" << tmp << ": " << f[n] << endl;
}
int main () {
    freopen ("A-small-attempt3.in", "r", stdin);
    freopen ("1.out", "w", stdout);
    cin >> t;
    f[1] = 1;
    for (int i=2; i<=1000000; i++)
        f[i] = maxint;
    for (int i=1; i<=999999; i++) {
        f[i+1] = min (f[i] + 1, f[i+1]);
        f[rev(i)] = min (f[rev(i)], f[i] + 1);
    }
    while (t) {
          ++tmp;
          solve ();
          t--;
          }    
}
