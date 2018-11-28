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
int t , n , m;
int arr [32 + 5];
ll res [16 + 5];

ll power (ll base , ll po){

    if(po == 0) return 1;
    if(po == 1) return base;
    ll ans;
    if(po % 2 == 0){
        ans = power(base , po / 2);
        return ans * ans;
    } else {
        return base * power(base , po - 1);
    }
}

void rec(int index){

    if(!m) return;

    if(index == n - 1){

        long long num = 0;
        bool found = false;
        int l = 0;

        for(int i = 2; i <= 10 && !found; i++){

            num = 0;
            for(int j = n - 1, k = 0; j >= 0; j--, k++){

                if(arr[j] == 0) continue;
                num+= power(i , k);
            }

            int sq = sqrt(num);
            bool flag = false;

            for(int j = 2; j <= sq; j++){

                if(num % j == 0){

                    flag = true;
                    res[l++] = j;
                    break;
                }
            }

            if(flag == false) found = true;
        }

        if(!found){

            m--;
            for(int i = 0; i < n; i++) printf("%d", arr[i]);
            printf(" ");
            for(int i = 0; i < 9; i++) printf("%lld ", res[i]);
            printf("\n");
        }

        return;
    }

    arr[index] = 0;
    rec(index + 1);
    arr[index] = 1;
    rec(index + 1);

}

int main()
{
    //ios::sync_with_stdio(false);cin.tie(0);

    freopen ("C-small-attempt0.in", "r", stdin);
    freopen ("ans.txt","w",stdout);


    scanf("%lld", &t);

    while(t--){

        printf("Case #1:\n");
        scanf("%d %d", &n , &m);
        arr[0] = 1;
        arr[n - 1] = 1;
        rec(1);
    }

    return 0;
}
