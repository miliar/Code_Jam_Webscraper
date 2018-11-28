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

bool arr [10 + 1];

int main()
{
    //ios::sync_with_stdio(false);cin.tie(0);

    freopen ("A-large (1).in", "r", stdin);
    freopen ("large.txt","w",stdout);

    ll n , m  , k , d , t , tem1 , tem2 , tem3 , tem4 , y = 1, sum = 0 , ans = 0;
    string s , c;

    scanf("%lld", &t);

    while(t--){

        memset(arr , false, sizeof arr);
        bool in = false;

        scanf("%lld", &n);
        printf("Case #%d: ", y++);

        if(n == 0){

            printf("INSOMNIA\n");
            continue;
        }

        for(long long i = 1; ; i++){

            ans = i * n;
            if(ans > 1e18){

                in = true;
                break;
            }

            bool en = true;
            sum = ans;

            while(sum != 0){

                d = sum % 10;
                arr[d] = true;
                sum /= 10;
            }

            for(int j = 0; j < 10; j++){

                if(!arr[j]){

                    en = false;
                    break;
                }
            }

            if(en) break;
        }


        if(in) printf("INSOMNIA\n");
        else {

            printf("%lld\n", ans);
        }

    }

    return 0;
}
