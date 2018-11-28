#include <bits/stdc++.h>

using namespace std;

#define mem0(arr) memset(arr , 0 , sizeof arr)
#define memf(arr) memset(arr , false , sizeof arr)
#define memdp(arr) memset(arr , -1 , sizeof arr)
#define rep(i , n) for(int i = 1; i <= n; i++)
#define loop(i , n) for(int i = 0; i < n; i++)
#define pb push_back
#define fi first
#define se second
#define cs(y) cout << "Case " << y << ": "
#define cs2(y) cout << "Case " << y << ":" << "\n"

typedef long long ll;

int main()
{
    //ios::sync_with_stdio(false);cin.tie(0);

    freopen ("D-small-attempt0.in", "r", stdin);
    freopen ("res.txt","w",stdout);

    int t, k , c , s, y = 1;

    scanf("%lld", &t);

    while(t--){

        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d: ", y++);

        if(c == 1){

            for(int i = 1; i <= k; i++) printf("%d ", i);
            printf("\n");
            continue;
        }

        for(int i = 1, j = 0; j < k; j++, i += k){

            printf("%d ", i);
        }

        printf("\n");
    }

    return 0;
}
