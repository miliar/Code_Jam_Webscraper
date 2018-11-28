#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef  long long LL;          
const int N = 105;
const int M = 20005;
const int INF = 1000000007;
int a[20];
int main () {
    #ifndef ONLINE_JUDGE
        freopen ("input.txt" , "r" , stdin);                                           
        freopen ("output.txt" , "w" , stdout);
    #endif
    int t , cas = 0;
    scanf ("%d" , &t);
    while (t --) {
        memset (a , 0 , sizeof (a));
        int r;scanf ("%d" , &r);
        for (int i = 0 ; i < 4 ; i ++) {
            for (int j = 0 ; j < 4 ; j ++) {
                int k;scanf ("%d" , &k);
                if (i + 1 == r) {
                    a[k] ++;
                }
            }
        }
        scanf ("%d" , &r);
        for (int i = 0 ; i < 4 ; i ++) {
            for (int j = 0 ; j < 4 ; j ++) {
                int k;scanf ("%d" , &k);
                if (i + 1 == r) {
                    a[k] ++;
                }
            }
        }
        vector <int> ans;
        for (int i = 1 ; i <= 16 ; i ++)
            if (a[i] == 2) {
                ans.push_back (i);
            }
        printf ("Case #%d: " , ++ cas);
        if (ans.size() == 0) puts ("Volunteer cheated!");
        else if (ans.size() == 1) printf ("%d\n" , ans[0]);
        else printf ("Bad magician!\n");
    }    
    return 0;
}