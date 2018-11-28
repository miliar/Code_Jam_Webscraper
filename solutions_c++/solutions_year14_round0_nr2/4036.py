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
const int MAXN = 111111;   
const ll MOD = 1E9 + 7;
                         
int tt;
double c, f, x, speed, cur, ans;

int main() {

	cout.precision(30);
    cin >> tt;
    forn(t, tt) {
    	printf("Case #%d: ", t + 1); 
    	cin >> c >> f >> x;

    	ans = x / 2;
    	speed = 2;
    	cur = 0;
    	forn(i, 5000000) {
    		cur += c / speed;
    		speed += f;
    		ans = min(ans, cur + x / speed);
        }

        cout << ans << '\n';
    }
	
    return 0;
}