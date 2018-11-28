#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <iomanip>
#include <list>
#include <stack>
#include <queue>
#include <bitset>
#include <numeric>
#include <functional>

#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cctype>
#include <cstdlib>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define rep(i, n)       for(int i = 0; i < n; i++)
#define reps(i, a, n)   for(int i = a; i < n; i++)
#define precout(a,b)    cout << fixed << setprecision((b)) << (a)
#define endl 			'\n'
#define pb              push_back
#define mp              make_pair
#define ff              first
#define ss              second
#define all(a)          a.begin(), a.end()
#define rall(a)			a.rbegin(), a.rend()
#define sz(x)			(int)x.size()
#define fastIO   		ios::sync_with_stdio(false); cin.tie(0);
#define isOn(S, j)      (S & (1 << j))
int N, J;

ll base(int b, ll msk) {
    ll ret = 0;
    ll s = 1;
    for (int i = 0; i < N; i++) {
        if (msk&(1<<i)) ret += s;
        s *= b;
    }
    return ret;
}



vector< ll > ans;
bool isprime(ll msk) {
    for(int b = 2; b <= 10; b++) {
        ll num = base(b, msk);
        //cout << num << endl;
        for (ll i = 2; i * i <= num; i++) {
            if (num % i == 0){
                ans.pb(i);
                break;
            }
        }
    }
    if (sz(ans) == 9) return true;
    return false;
}



int main(){
#ifndef ONLINE_JUDGE
    const clock_t begin_time = clock();
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    fastIO
    
    
    int t;
    cin >> t;

    for (int T = 1; T <= t; T++) {
        cout << "Case #" << T << ": " << endl;
        ans.clear();
        cin >> N >> J;
        int found = 0;
        for (ll msk = 0; msk <= 1<<N && found < J; msk++) {
            if (not (msk & (1 << 0))) continue;
            if (not (msk & (1 << (N - 1)))) continue;
           
            if (isprime(msk)) {
                found++;
                for (int i = N - 1; i >= 0; i--) {
                    if(isOn(msk, i)) cout << 1;
                    else cout << 0;
                }
                cout << " ";
                for (auto x : ans) cout << x << " ";
                cout << endl;
            }
            ans.clear();
            
        }
        
    }
    
#ifndef ONLINE_JUDGE
   	cout << endl;
    cout << "Time : ";
    cout << float( clock () - begin_time ) / CLOCKS_PER_SEC << endl;
#endif
    
    return 0;
}