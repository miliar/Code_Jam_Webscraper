#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll i, j, k, x, y, z, m, n, ans, p, q, r, c, s, t;


int main()
{
    freopen("D-small-attempt0.txt", "r", stdin);
    freopen("D-small-attempt0output.txt", "w", stdout);

    cin >> t;
    int cs = 1;

    while(t--){

        cin >> k >> c >> s;

        printf("Case #%d: ", cs++);

        ll temp = 1;

        for(i = 1; i < c; i++){
            temp = temp * k;
        }

        for(i = 1, j = 1; j <= s; i += temp, j++) printf("%lld ", i);


        cout << endl;

    }


    return 0;
}
