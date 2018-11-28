#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#ifndef ONLINE_JUDGE
	#define gc getchar
#else
	#define gc getchar_unlocked
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef pair<int,int> ii;

#define inf 2147483647
#define linf (ll)(1e18)
#define eps (double)(1e-9)
#define leps (ld)(1e-18)
#define PI (double)(3.141592653589793238)
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

int main (void) {

    #ifndef ONLINE_JUDGE
    	freopen ("input.txt", "r", stdin);
    #endif // ONLINE_JUDGE
    int t, ca;
    double c, f, x, t1, t2, r, temp;
    cin >> t;
    ca = 0;
    while(t--) {
        cin >> c >> f >> x;
        r = 2.0;
        t1 = x / r; t2 = 0.0;
        while(true) {
            t2 += c / r;
            temp = x / (r + f);
            if((t2 + temp) >= t1) {
                break;
            }
            t1 = t2 + temp;
            r += f;
        }
        printf("Case #%d: %f\n", (++ca), t1);
    }
    return 0;
}