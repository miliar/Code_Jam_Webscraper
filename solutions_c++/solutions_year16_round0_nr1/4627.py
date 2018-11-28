#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll i, j, k, l, x, y, z, ans, t;

map < ll, ll > cnt;

bool chk(ll x)
{
    while(x != 0){
       y = x % 10;
       x = x / 10;
       cnt[y] = 1;
    }

    for(int i = 0; i < 10; i++){
        if(!cnt[i]) return false;
    }

    return true;

}

int main()
{

    freopen("A-large.txt", "r", stdin);
    freopen("A-large_output.txt", "w", stdout);
    cin >> t;
    int cs = 1;

    while(t--){
        cin >> x;
        cnt.clear();

        printf("Case #%d: ", cs++);

        if(x == 0){
            printf("INSOMNIA\n");
            continue;
        }

        for(i = 1; ;i++){

            bool flag = chk(x * i);

            if(flag == true){
                printf("%lld\n", x * i);
                break;
            }

        }


    }


    return 0;
}
