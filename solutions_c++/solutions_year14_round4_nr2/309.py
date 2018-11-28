#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <vector>
#include <sstream>
#include <set>
#include <ctime>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
const int N = 1005;
const int MOD = 1000000007;
int n , a[N];
pair <int , int> b[N];
int main(){
    // freopen("B-large.in" , "r" , stdin);
    // freopen("B.out" , "w" , stdout);
    int t , cas = 0;
    scanf ("%d" , &t);
    while (t --) {
        scanf ("%d" , &n);
        for (int i = 0 ; i < n ; i ++) {
            scanf ("%d" , &a[i]);
        }
        sort (b , b + n);
        int ans = 0;
        for (int i = 0 , l = 0 , r = n - 1 ; i < n ; i ++) {
            int mn = a[l] , pos = l;
            for (int j = l + 1 ; j <= r ; j ++) {
                if (a[j] < mn) {
                    mn = a[j];
                    pos = j;
                }
            }

            int L = abs (pos - l) , R = abs (pos - r);
            if (L <= R) {
                ans += L;
                while (pos > l) {
                    swap (a[pos] , a[pos - 1]);
                    pos --;
                }
                l ++;
            }
            else {
                ans += R;
                while (pos < r) {
                    swap (a[pos] , a[pos + 1]);
                    pos ++;
                }
                r --;
            }
            // cout << ans << " " << l << " " << r << endl;
        }
        printf ("Case #%d: %d\n" , ++ cas , ans);
    }
    return 0;
}
