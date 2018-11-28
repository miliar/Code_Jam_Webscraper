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

int n;
ll mini = - (1LL<<63);
string s;

bool allGood() {
    for (int i = 0; i < n; i++)
        if (s[i] == '-') return false;
    
    return true;
}

void flip(int i) {
    //reverse(s.begin(), s.begin() + i);
    rep(j, i + 1)
        if (s[j] == '+') s[j] = '-';
        else s[j] = '+';
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
        cout << "Case #" << T << ": ";
        cin >> s;
        n = sz(s);
        int ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (allGood()) break;
            if (s[i] == '-') {
                ans++;
                flip(i);
            }
        }

        cout << ans << endl;
        
    }
    
#ifndef ONLINE_JUDGE
   	cout << endl;
    cout << "Time : ";
    cout << float( clock () - begin_time ) / CLOCKS_PER_SEC << endl;
#endif
    
    return 0;
}