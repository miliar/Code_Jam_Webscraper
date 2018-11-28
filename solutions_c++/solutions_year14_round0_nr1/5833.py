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

	int T,x,y;
	cin >> T;
    FOR(t,1,T+1) {
        cin >> x;
        --x;
        int a[4][4];
        int cnt[17] = {0};
        FOR(i,0,4) FOR(j,0,4) cin >> a[i][j];
        FOR(i,0,4) cnt[a[x][i]]++;
        cin >> y;
        --y;
        FOR(i,0,4) FOR(j,0,4) cin >> a[i][j];
        FOR(i,0,4) cnt[a[y][i]]++;
        vi v;
        FOR(i,1,17) if (cnt[i] >= 2) v.pb(i);
        if (v.size() == 1) cout << "Case #" << t << ": " << v[0] << endl;
        else if (v.size() > 1) cout << "Case #" << t << ": Bad magician!" << endl;
        else cout << "Case #" << t << ": Volunteer cheated!" << endl;
    }
	return 0;
}
