#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <iomanip>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())
#define endl        '\n'

typedef long long			ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>			vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>			vpii;

const int MX = 25;

int main(int argc, char *argv[])
{
#ifndef ONLINE_JUDGE
	freopen(argv[1],"r",stdin);
#endif
#ifndef ONLINE_JUDGE
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

    cout << setprecision(7);
    cout << fixed;
	int T,x,y;
    double C,F,X;
	cin >> T;
    FOR(t,1,T+1) {
        cin >> C >> F >> X;
        int k = 0;
        while (true) {
            if (2*C + k*(F*C+F*X) + C*F >= k*F*X + X*F) break;
            ++k;
        }
        double ans = 0;
        int r = 2;
        FOR(i,0,k) ans += C/(r+i*F);
        ans += X/(r+k*F);
        cout << "Case #" << t << ": " << ans << endl;
    }
	return 0;
}
