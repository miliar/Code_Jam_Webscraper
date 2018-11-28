#include <iostream>
#include <string>
#include <stdio.h>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>

using namespace std;
typedef long long ll;
typedef long double ld;
#define MOD (ld)1e9 + 7
#define PI (ld)3.14159265358979324
#define mp make_pair 
#define pb push_back
#define ft first
#define sd second
#define sz(a) (ll)a.size()
#define pii pair<int,int>
#define pll pair<ll,ll>
#define loop(i, n) for(int (i) = 0; (i) < (n) ; ++ (i))
#define forn(i, l, r) for(int (i) = (l); (i) < (r) ; ++ (i))
#define vec vector 
#define str string
#define vii vector<int> 

vec<bool> used(10);
int check(ll val) {
    int ans = 0;
    while(val > 0) {
        if(!used[val % 10]) {
            ++ans;
            used[val % 10] = true;
        }
        val /= 10;
    }
    return ans;
}

void solve() {
    used.clear();
    used.resize(10,false);
    int count = 0;
    ll n;
    cin >> n;
    if(n == 0) {
        cout << "INSOMNIA" <<endl;
        return;
    }
    
    ll cur = 0;
    while(count < 10) {
        cur += n;
        count += check(cur);
    }
    cout << cur << endl;
}   

int main()
{
    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
    // cout << fixed;
    // cout.precision(3);
    ios_base::sync_with_stdio(false);   
    int t;
    cin >> t;
    loop(i,t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}