#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <cctype>
#include <list>

#define INF 2000000000
#define ll long long
#define PI 3.1415926535897932384626433832795
#define all(a) a.begin(), a.end()
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define y1 olololo1
#define y0 olololo2
#define m0(a) memset(a,0,sizeof(a))

using namespace std;
const long long LLINF = 9223372036854775806;



int t;
int cnt = 0, d[10000001];



bool ok(ll x){
    int dig[100], cnt=0;
    while (x>0){
        ++cnt;
        dig[cnt]=x%10;
        x/=10;
    }
    bool res=1;
    for (int i=1; i<=cnt/2; ++i)
        res&=(dig[i]==dig[cnt-i+1]);
    return res;
}

void solve(){
    ll a, b;
    cin >> a >> b;
    ll res = 0;
    for (ll i=1; i*i<=b; ++i){
        if (!ok(i)) continue;
        ll next =i*i;
        if (!ok(next)) continue;
        if (next >= a && next <= b) ++res;
    }
    cout << res;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    for (int it = 1; it <= t; ++it){
        cout << "Case #"<<it << ": ";
        solve();
        cout << "\n";
    }
    
    
    return 0;
    
}