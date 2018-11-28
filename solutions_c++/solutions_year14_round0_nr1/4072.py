#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <deque>
#include <numeric>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <sys/time.h>
#include <regex.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> VI;
typedef vector<VI> VVI;

int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC , tc = 1;
	cin >> TC;
	while(TC-->0)
	{
		set<int> S1;
		VVI mat(4,4);
		int r1; cin >> r1;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				cin >> mat[i][j];
				if(r1-1 == i)
					S1.insert(mat[i][j]);
			}		
		}
		int r2; cin >> r2;
		set<int> S2;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				cin >> mat[i][j];
				if(r2-1 == i)
					S2.insert(mat[i][j]);
			}		
		}
		vector<int> ans(4);
		vector<int>::iterator it = set_intersection(S1.begin(),S1.end(),S2.begin(),S2.end(),ans.begin());
		ans.resize(it - ans.begin());
		cout << "Case #" << tc++ << ": ";
		if(ans.size() == 0)
			cout << "Volunteer cheated!" << endl;
		else if(ans.size() > 1)
			cout << "Bad magician!" << endl;
		else
			cout << ans[0] << endl;
	}
}







