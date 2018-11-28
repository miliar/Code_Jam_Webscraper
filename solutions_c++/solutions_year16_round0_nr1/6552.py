#include<bits/stdc++.h>
using namespace std;
#define ll long long
int used[10];
ll solve(ll x){
    ll curr = x;
    int numbers = 0;
    memset(used, 0, sizeof(used));
    for(int i=0; i<10000; ++i){
        ll tmp = curr;
        while(tmp){
            int digit = tmp%10;
            if(used[digit] == 0){
                numbers++;
            }
            used[digit] = 1;
            tmp/=10;
        }
        if(numbers == 10){
            return curr;
        }
        curr+=x;
    }
    return -1;
}
int main () {
    ios_base::sync_with_stdio(false);
    freopen("C:\\in.txt","r", stdin);
    freopen("C:\\gcj2016\\out.txt", "w", stdout);
    memset(used, 0, sizeof(used));
    int TC;
    cin >> TC;
    for(int t = 1; t<=TC; ++t){
        int x;
        cin >> x;
        cout << "Case #" << t << ": ";
        if(x == 0) {
            cout << "INSOMNIA";
        } else {
            cout << solve(x);
        }
        cout << endl;
    }

    return 0;
}
