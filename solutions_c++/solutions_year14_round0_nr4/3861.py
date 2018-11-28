#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cmath>
#include <iomanip>
#include <cassert>
                   
using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++) 
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = int(a); i < int(b); i++)

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;

const int INF = 1E9;   
const ld eps = 1e-6;
const ld pi = acos(-1.0);
const int MAXN = 10;   
const ll MOD = 1E9 + 7;
const int dx[] = {0, 0, -1, 1};
const int dy[] = {-1, 1, 0, 0};
                         
int tt, n, ans[2];
vector<double> a[2];
vi used;
bool f;

int main() {

	cout.precision(30);
    cin >> tt;
    forn(t, tt) {
    	printf("Case #%d: ", t + 1);
    	
    	cin >> n;
    	used.clear();
    	used.resize(n, 0);

    	forn(i, 2) {
    		a[i].clear();
    		a[i].resize(n);
    		forn(j, n)
    			cin >> a[i][j];
    		sort(all(a[i]));
    	}

    	ans[0] = ans[1] = 0;
    	f = 0;
    	for (int i = 0; i < n; i++) {
    		f = 1;
    		for (int j = n - 1; j >= i; j--) {
    			if (a[0][j] <= a[1][j - i]) {
    				f = 0;
    				break;
    			}
    		}	

    		if (f) {
    			ans[0] = n - i;
    			break;
    		}
    	}

    	for (int i = 0; i < n; i++) {
    		f = 0;
    		for (int j = 0; j < n; j++)
    			if (!used[j]) {
    				if (a[1][j] > a[0][i]) {
    					f = 1;
    					used[j] = 1;
    					break;
    				}
    			}	

    		if (!f) {
    			ans[1]++;
    			forn(j, n)
    				if (!used[j]) {
    					used[j] = 1;
    					break;
    				}
    		}
    	}

    	cout << ans[0] << ' ' << ans[1] << '\n';
    }
	
    return 0;
}