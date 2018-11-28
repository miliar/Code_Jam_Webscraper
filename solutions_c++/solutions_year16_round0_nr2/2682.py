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


void solve() {
    int ans = 0;
    bool fst = 1;
    bool fins = 0;
    string s;
    cin >> s;
    loop(i,sz(s)) {
        if(s[i] == '-') {
            if(!fins) {
                fins = 1;
                if(fst) {
                    ++ans;
                } else {
                    ans += 2;
                    fst = 0;
                }
            }
        } else {
            fins = 0;
            fst = 0;
        }
    }
    cout << ans << '\n';
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

