#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>
#include <string>
#include <cmath>
#include <map>
#include <set>
#define MOD 1e9 + 7
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define sz(a) a.size()
#define loop(i, n) for(long long (i) = 0; (i) < (n) ; ++ (i))
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>  
typedef long long ll;
typedef long double ld;

using namespace std;


/*@Sergey_Miller*/

int sum = 0;
int dig[10];

bool next(ll k) {
    while(k) {
        int r = k%10;
        if(!dig[r]) {
            dig[r] = 1;
            ++sum;
            if(sum == 10) {
                return true;
            }
        }
        k/=10;
    }
    return false;
}

void solve() {
    ll x;
    cin >> x;
    sum = 0;
    ll k = x;
    loop(i,10) {
        dig[i] = 0;
    }
    if(x == 0) {
    cout << "INSOMNIA\n";
    return;
    } else {
    while(!next(k)) {
        k += x;
    }
    }
    cout << k << '\n';
}


int main () {
    ios::sync_with_stdio(false);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    loop(i,n) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}

