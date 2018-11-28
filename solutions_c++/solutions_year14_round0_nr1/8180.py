/* Paras Narang 
 *
 */
#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <deque>
#include <bitset>
#include <cmath>
#include <set>
#include <sstream>

using namespace std;

#define oo 0x7F7F7F7F
#define LET(x,a)     __typeof(a) x(a)
#define EACH(it,v)   for(LET(it,v.begin());it!=v.end();++it)
#define REP(i,n)     for(__typeof(n) i(0); i<n; i++)
#define FOR(i,j,n)   for(__typeof(n) i(j); i<n; i++)
#define ALL(x)       (x).begin(), (x).end()
#define gint(t)      scanf("%d", &t);
#define pint(t)      printf("%d\n", t);
#define pb           push_back
#define mp           make_pair

typedef long long int   ll;
typedef unsigned long long int ull;
typedef unsigned int    uint;
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector<vi>      vii;
typedef vector<pii>     vpii;

vi intersection(vi &v1, vi &v2){
	vi v3;
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),back_inserter(v3));
	return v3;
}

int main() {
    int t; gint(t);
    REP(ti, t) {
    	int cards[4][4];
    	vi options1, options2;
  
	    int ans1; cin >> ans1;
	    REP(xi, 4){
		    REP(yi, 4){
		    	cin >> cards[xi][yi];
			if(xi == ans1-1)
				options1.pb(cards[xi][yi]);
		    }
	    }

	    int ans2; cin >> ans2;
	    REP(xi, 4){
		    REP(yi, 4){
		    	cin >> cards[xi][yi];
			if(xi == ans2-1){
				options2.pb(cards[xi][yi]);
			}
		    }
	    }
	    vi ans = intersection(options1, options2);
	    cout << "Case #" << ti+1 << ": ";
	    int len = ans.size();
	    //EACH(it, ans) cout << *it << " ";
	    if(len == 1){
	    	cout << ans[0] << endl;
	    }
	    else if(len == 0){
	    	cout << "Volunteer cheated!" << endl;
	    }
	    else{
	    	cout << "Bad magician!" << endl;
	    }
    }
    return 0;
}
