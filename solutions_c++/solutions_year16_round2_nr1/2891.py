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
		string in; cin >> in;
		VI freq(26, 0);
		VI ans(10, 0);

		REP(i, in.sz) freq[in[i] - 'A']++;

		if(freq['G'-'A'] > 0)
		{
			ans[8] = freq['G'-'A'];
			freq['E'-'A'] -= ans[8];
			freq['I'-'A'] -= ans[8];
			freq['G'-'A'] -= ans[8];
			freq['H'-'A'] -= ans[8];
			freq['T'-'A'] -= ans[8];
		}

		if(freq['Z'-'A'] > 0)
		{
			ans[0] = freq['Z'-'A'];
			freq['Z'-'A'] -= ans[0];
			freq['E'-'A'] -= ans[0];
			freq['R'-'A'] -= ans[0];
			freq['O'-'A'] -= ans[0];
		}

		if(freq['W'-'A'] > 0)
		{
			ans[2] = freq['W'-'A'];
			freq['T'-'A'] -= ans[2];
			freq['W'-'A'] -= ans[2];
			freq['O'-'A'] -= ans[2];
		}

		if(freq['U'-'A'] > 0)
		{
			ans[4] = freq['U'-'A'];
			freq['F'-'A'] -= ans[4];
			freq['O'-'A'] -= ans[4];
			freq['R'-'A'] -= ans[4];
			freq['U'-'A'] -= ans[4];
		}

		if(freq['X'-'A'] > 0)
		{
			ans[6] = freq['X'-'A'];
			freq['S'-'A'] -= ans[6];
			freq['I'-'A'] -= ans[6];
			freq['X'-'A'] -= ans[6];
		}

		if(freq['H'-'A'] > 0)
		{
			ans[3] = freq['H'-'A'];
			freq['T'-'A'] -= ans[3];
			freq['H'-'A'] -= ans[3];
			freq['R'-'A'] -= ans[3];
			freq['E'-'A'] -= ans[3];
			freq['E'-'A'] -= ans[3];
		}

		if(freq['O'-'A'] > 0)
		{
			ans[1] = freq['O'-'A'];
			freq['O'-'A'] -= ans[1];
			freq['N'-'A'] -= ans[1];
			freq['E'-'A'] -= ans[1];
		}

		if(freq['F'-'A'] > 0) 
		{
			ans[5] = freq['F'-'A'];
			freq['F'-'A'] -= ans[5];
			freq['I'-'A'] -= ans[5];
			freq['V'-'A'] -= ans[5];
			freq['E'-'A'] -= ans[5];
		}

		if(freq['V'-'A'] > 0)
		{
			ans[7] = freq['V'-'A'];
			freq['S'-'A'] -= ans[7];
			freq['E'-'A'] -= ans[7];
			freq['V'-'A'] -= ans[7];
			freq['E'-'A'] -= ans[7];
			freq['N'-'A'] -= ans[7];
		}

		if(freq['I'-'A'] > 0) 
		{
			ans[9] = freq['I'-'A'];
			freq['N'-'A'] -= ans[9];
			freq['I'-'A'] -= ans[9];
			freq['N'-'A'] -= ans[9];
			freq['E'-'A'] -= ans[9];
		}

		cout << "Case #" << c+1 << ": ";
		REP(i,10)
		{
			REP(j,ans[i])
				cout<<i;

		}
		cout << "\n";
		}

		return 0;
	}
