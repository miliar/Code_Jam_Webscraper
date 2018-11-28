#include <bits/stdc++.h> 

using namespace std;
 
#define sz(c) (int)(c).size()
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
 
#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef unsigned int uint;

#ifdef WIN32
#define I64 "%I64d"
#else
#define I64 "%lld"
#endif

#define FNAME "1"

int T, n, b[100005];
char s[100005];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout); 
    scanf("%d", &T);
    for (int t = 0; t < T; t++)
    {
        scanf("%d%s", &n, s);
        int sz = 0;
        for (int i = 0; i < n + 1; i++)
            for (int j = 0; j < s[i] - '0'; j++)
                b[sz++] = i;
        int ans = 0;
        for (int i = 0; i < sz; i++)
            ans = max(ans, b[i] - i);
        printf("Case #%d: %d\n", t + 1, ans);
    }    
    return 0;
}