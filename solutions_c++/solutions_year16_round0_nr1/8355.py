#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit atof atoi 
#include <cstdio>		// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>		// require fabs
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>		// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>		// require srand
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()
#define each(i,c) for(auto i=(c).begin();i!=(c).end();++i)
#define exist(s,e) ((s).find(e)!=(s).end())
#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizoef(a))
#define sz(s) (int)((s).size())
#define INRANGE(x,s,e) ((s)<=(x) && (x)<(e))
#define pb push_back
#define MP(x,y) make_pair((x),(y))

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int solve(int n){
	bool digit[10] = {false};
	for (int i = 1; i < 100; ++i){
		int curr = i * n;
		while(curr > 0){
			digit[curr % 10] |= true;
			curr /= 10;
		} // end while
		bool ok = true;
		rep (j, 10){
			if (!digit[j]){
				ok = false;
				break;
			} // end if
		} // end rep
		if (ok) return i*n;
	} // end for
	return -1;
} 

int main()
{
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	vector<int> number(T,0);
	vector<int> answer(T,-1);

	rep (i, T){
		cin >> number[i];
		if (number[i] == 0) continue;
		answer[i] = solve(number[i]);			
	} // end rep
	rep (i, T){
		cout << "Case #" << i+1 << ": ";
		if (answer[i] == -1){
			cout << "INSOMNIA";
		}else{
			cout << answer[i];
		} // end if
		cout << endl;
	} // end rep

	return 0;
}
