#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(x) (x) * (x)
#define forn(i, l, r) for(int i = l; i < r; i ++)                      
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it ++)
#define y1 salnk
#define N 200100              
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;


int w[20];
ll t, n;
bool ok(ll x) {
 	while (x) {
 	 	w[x % 10] = 1;
 	 	x /= 10;
 	}
 	for (int i = 0; i < 10; i++)
 		if (!w[i]) return 0;
 	return 1;
}
int main () {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    cin >> t;
    int qq = 0;
    while (t--) {
    	qq++;
    	for (int i = 0; i < 10; i++)
    		w[i] = 0;
     	cin >> n;
     	printf("Case #%d: ", qq);
     	if (n == 0) {
     	 	printf("INSOMNIA\n");
     	 	continue;
     	}
     	for (int i = 1; ; i++) {
     	 	if (ok(n * i * 1ll))  {
     	 		cout << n * 1ll * i << endl;
     	 		break;
     	 	}
     	}
    }
    return 0;
}