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
    int t, f, s, d, i, j, count, c, res;
    scanf("%d", &t);
    vvi one(4, vi(4)); vvi two(4, vi(4));
    c = 0;
    while(t--) {
        ++c;
        count = 0;

        scanf("%d", &f); --f;
        
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) {
                cin >> one[i][j];
            }
        }

        scanf("%d", &s); --s;
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) {
                cin >> two[i][j];
            }
        }
        
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) {
                if(one[f][i] == two[s][j]) {
                    ++count;
                    res = one[f][i];
                }
            }
        }
        if(count == 0) {
            printf("Case #%d: Volunteer cheated!\n", c);
        }
        else if(count == 1) {
            printf("Case #%d: %d\n", c, res);
        }
        else {
            printf("Case #%d: Bad magician!\n", c);
        }

    }
    return 0;
}