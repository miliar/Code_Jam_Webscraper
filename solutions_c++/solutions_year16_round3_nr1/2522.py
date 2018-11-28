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
		//vector < pair <int, char> > s;
		priority_queue <pair<int, char>, vector < pair < int, char > > > PQ;
		int N; cin >> N;

		REP(i, N) 
		{
			int x; cin >> x;
			PI p = make_pair(x, i + 'A');
			//s.pb(p);
			PQ.push(p);
		}
		cout << "Case #" << c+1 << ": ";

//		while(!PQ.empty())
//		{
//			cout << PQ.top().first << " " << PQ.top().second << "\n";
//			PQ.pop();
//		}

		while(!PQ.empty())
		{
			pair <int, char> ans = PQ.top();
			if(ans.first <= 0)
			{
				PQ.pop();
				continue;
			}

			if(PQ.sz == 2)
			{
				pair <int, char> p1, p2;
				p1 = PQ.top(); PQ.pop();
				p2 = PQ.top(); PQ.pop();

				if(p1.first ==  p2.first)
				{
					cout << p1.second << p2.second << " ";
					pair <int, char> y1 = make_pair(p1.first-1, p1.second);
					pair <int, char> y2 = make_pair(p2.first-1, p2.second);
					PQ.push(y1);
					PQ.push(y2);
					continue;
				}
				else
				{
					PQ.push(p1);
					PQ.push(p2);
				}
			}

			cout << ans.second << " ";
			PQ.pop();
			pair <int, char> y = make_pair(ans.first-1, ans.second);
			if(y.first > 0)
			PQ.push(y);
		}
		cout << "\n";



	}

	return 0;
}
