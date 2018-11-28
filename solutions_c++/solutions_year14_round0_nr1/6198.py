#include <vector>
#include <queue>
#include <climits>
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
#include <cstring>
 
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long LL;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef pair <int, int> PI;
typedef vector <PI> VPI;


int main()
{
	int T;cin >> T;
	REP(c,T)
	{
		// Begin code
		int r1;cin >> r1;
		int board[4][4];
		int cnt1[16] = {0};

		REP(i,4) REP(j,4)
		cin >> board[i][j];

		REP(i,4)
		cnt1[board[r1-1][i]-1]++;

		int r2;cin >> r2;
		REP(i,4) REP(j,4)
		cin >> board[i][j];

		int cnt2[16] = {0};
		REP(i,4)
		cnt2[board[r2-1][i]-1]++;

		int match = 0, idx = -1;

		REP(i,16) if(cnt1[i] == 1 && (cnt1[i] == cnt2[i])) 
		{
			match++;
			idx = i;
		}

		cout << "Case #" << c+1 << ": ";
		if(match == 1 && idx != -1)
		cout << idx+1 << endl;
		else if(match == 0) 
		cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;
	}

	return 0;
}
