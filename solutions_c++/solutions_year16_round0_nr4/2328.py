#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f first
#define s second

int a[100];

int main(){

    freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("ans.out","w",stdout);
    int t;
    scanf("%d", &t);
    for(int z = 1; z <= t; ++z){

        ll k , c, s;
        cin >> k >> c >> s;
        printf("Case #%d: " , z);
        ll ans = 1;
        ll shift = 1;
        for(int i = 0; i < c-1; ++i)shift *= k;
        for(int i = 0; i < k; ++i){
            cout << ans << " ";
            ans += shift;
        }
        cout << "\n";
    }

    return 0;
}
