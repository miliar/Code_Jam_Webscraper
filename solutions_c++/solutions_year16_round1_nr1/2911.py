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

void SolveTestCase(int T){
	// write your solution here
	string S;
	cin >> S;

	string A = "";
	FOR(i, 0, S.length()){
		if (A == "")
			A += S[i];
		else {
			if (S[i] >= A[0])
				A = S[i] + A;
			else 
				A = A + S[i];
		}
	}
	
	cout << "Case #" << T << ": " << A << endl;
}

int main()
{
	std::ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	FOR(t, 0, T)
		SolveTestCase(t+1);

	return 0;
}
