#include "cstdio"
#include "cstring"
#include "iostream"
#include "string"
#include "vector"
#include "algorithm"
using namespace std;

const int MAXN = 10005;
int n;
int x;
int s[MAXN];
int main()
{
    //freopen("C:\\Users\\humo.xpx\\Desktop\\A-small-attempt0.in","r",stdin);
    //freopen("C:\\Users\\humo.xpx\\Desktop\\out.txt","w",stdout);
    int T, cas = 0;
    scanf ("%d", &T);
    while (T--) {
        scanf ("%d%d", &n, &x);
        for (int i = 0; i < n; i ++){
            scanf ("%d", &s[i]);
        }
        sort (s, s + n);
        int i = 0, j = n - 1;
        int ans = 0;
        while ( i <= j ) {
            if (i == j) {
                ans ++;
                break;
            }
            if (s[i] + s[j] <= x) {
                ans ++;
                i ++;
                j --;
            }else {
                j --;
                ans ++;
            }
        }
        printf ("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
