/* g++ */

/* input/output streams and formatting */
	#include <iostream>
	#include <cstdio>
	#include <sstream>
	#include <iomanip>

/* data structures */
	#include <vector>
	#include <map>
	#include <stack>
	#include <queue>
	#include <deque>
	#include <set>
	#include <bitset>	

/* useful libs */
	#include <cstdlib>
	#include <algorithm>
	#include <cmath>

/* don't use this shit in your projects, 
 * it's only useful in olympiads ! 
 */
	using namespace std;

/* some useful defines */
	#define MAX(x, y) ( ((x) > (y))? (x):(y) )
	#define MIN(x, y) ( ((x) < (y))? (x):(y) )
	#define X first
	#define Y second
	#define PB(x) push_back(x)
	#define PPB(x) pop_back(x)
	#define MP(x, y) make_pair((x), (y))
	#define ALL(a) (a).begin(), (a).end()
	#define SORT(a) sort(ALL(a))
	#define FOR(i, a, b) for(int i=(a); i<(b); i++)
	#define SWAP(t, a, b) {(t) tmp=(a); (a)=(b); (b)=tmp;}
	#define EPS 0.0000001




int solve(vector<int>::iterator a, vector<int>::iterator b, int c){
	// we have to make all symbols equal to c
	int ans = 0;
	while (a != b && (*a) == c) a++;
	if (a != b){
		ans += solve(a, b, 1-c);
			// now the top b-a are equal to 1-c, need 1 more flip
		ans += 1;
	}
	return ans;
}

void SolveTestCase(int T){
	string s;
	cin >> s;
	reverse(s.begin(), s.end());
	vector<int> v(s.length());
	FOR(i, 0, s.length()){
		if (s[i] == '+') v[i] = 1;
		if (s[i] == '-') v[i] = 0;
	}
	
	cout << "Case #" << T << ": " << solve(v.begin(), v.end(), 1) << endl;
}

int main()
{
	std::ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	FOR(t, 0, T){
		SolveTestCase(t+1);
	}

	return 0;
}
