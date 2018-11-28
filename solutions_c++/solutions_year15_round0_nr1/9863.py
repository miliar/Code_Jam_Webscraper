#include <bits/stdc++.h>
#define ll long long int
#define MOD 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>

using namespace std;

int main(){
    ll t; cin >> t;
    for(int j=1; j<=t; j++){
         ll n;
         string s;
         cin >> n >> s;
         ll ans = 0;
         ll cur = 0;
         for(int i=0; i<=n; i++){
             if(cur < i){
                ans += (i - cur);
                cur += (i - cur);
             }
             cur += (s[i] - '0');
         }
         cout << "Case #" << j << ": " << ans << endl;
    }
}
