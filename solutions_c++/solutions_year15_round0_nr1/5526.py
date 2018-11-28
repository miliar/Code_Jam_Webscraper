#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <stdio.h>
#include <stack>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <set>
#include <iterator>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <iomanip>
#include <ctime>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define mp(a, b) make_pair(a, b)
#define sqr(x) ( (x) * (x) )
#define all(a) a.begin(), a.end()
#define ft first
#define sc second

typedef long long ll; 
typedef double ld;
typedef vector<int> vi; 
typedef vector<vi> vii; 
typedef pair<int, int> pii;

const int INF = 1e9;
const ll INF64 = 1e18;
const ld PI = acos(-1.0);
const int MOD = 1000000007;
const int N = 1001;

int n;
int a[N], b[N];

bool can(int k) {
    forn(i, n)
        b[i] = a[i];

    forn(i, k + 1) {
        bool ok = true;
        forn(j, n)
            ok &= (b[j] <= k - i);

        if (ok) return true;

        int pos = 0;
        forn(j, n)
            if (b[pos] < b[j])
                pos = j;
        b[pos] = (b[pos] + 1) / 2;        
    }

    return false;
}

int main() {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);   
#endif

    int T;
    cin >> T;
    forn(t, T) {
        int n;
        string s;

        cin >> n >> s;   

        int cur = s[0] - '0';
        int res = 0;

        for(int i = 1; i <= n; i++) {
            int c = s[i] - '0';
            if (c && cur < i) {
                res += i - cur;
                cur += i - cur;
                cur += c;
            } else {
                cur += c;
            }
        }

        cout << "Case #" << t + 1 << ": " << res << endl;
    }   

    /*int T;
    cin >> T;
    forn(t, T) {
        cin >> n;
        forn(i, n)
            cin >> a[i];

        int l = 1, r = 1e4;
        while (r - l > 1) {
            int mid = (r + l) / 2;
            if (can(mid))
                r = mid;
            else
                l = mid;
        }

        for(int i = l; i <= r; i++) {
            if (can(i)) {
                cout << "Case #" << t + 1 << ": " << i << endl;
            }
        }
    }*/
    
    return 0;
}