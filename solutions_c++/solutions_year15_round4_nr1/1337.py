#include <iostream> // strings/streams
#include <string>
#include <sstream>
#include <vector> // datastructures
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <tuple> // quick compare
#include <cstdio> // utils
#include <numeric>
#include <iterator>
#include <algorithm>
#include <math.h>
#include <chrono>
#include <assert.h>

#define REP(i,n)	for(decltype(n) i(0); i<(n); i++)
#define ITER(i,v)	for(auto&& i : v) // may be non-const!
#define ITERI(it,v)	for(auto it = begin(v); it != end(v);it++)
#define F(v)		begin(v), end(v)

using namespace std;
using vi = vector<int>;

constexpr bool LOG = false;
template<class T> void Log(T t){if(LOG) cerr << t << "\n";}
template<class T, class... S> void Log(T t, S... s){
	if(LOG) cerr << t <<"\t", Log(s...);
}
/* ============== END OF HEADER ============== */

int R,C;
array<array<char,100>,100> b;
array<array<bool,100>,100> m;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	int TC;
	cin >> TC;
	for(int tc=1; tc<=TC;tc++){
		cin >> R >> C;
		REP(i,100) m[i].fill(false);
		REP(i,R) REP(j,C)
			cin >> ws >> b[i][j];
		// check for arrows pointing off the board
		// left edge
		bool error = false;
		REP(r,R){
			REP(c,C){
				if(b[r][c] != '.'){
					if(b[r][c] == '<')
						b[r][c] = '^', m[r][c] = true;
					break;

				}
			}
		}
		REP(c,C){
			REP(r,R){
				if(b[r][c] != '.'){
					if(b[r][c] == '^')
						b[r][c] = '>', m[r][c] = true;
					break;
				}
			}
		}
		REP(r,R){
			for(int c = C-1; c>=0; c--){
				if(b[r][c] != '.'){
					if(b[r][c] == '>')
						b[r][c] = 'v', m[r][c] = true;
					break;
				}
			}
		}
		REP(c,C){
			for(int r = R-1; r>=0; r--){
				if(b[r][c] != '.'){
					if(b[r][c] == 'v')
						b[r][c] = '<', m[r][c] = true;
					break;
				}
			}
		}
		REP(r,R){
			REP(c,C){
				if(b[r][c] != '.'){
					if(b[r][c] == '<')
						b[r][c] = '^', m[r][c] = true;
					break;
				}
			}
		}
		REP(c,C){
			REP(r,R){
				if(b[r][c] != '.'){
					if(b[r][c] == '^')
						b[r][c] = '>', m[r][c] = true;
					break;
				}
			}
		}
		REP(r,R){
			for(int c = C-1; c>=0; c--){
				if(b[r][c] != '.'){
					if(b[r][c] == '>')
						b[r][c] = 'v', m[r][c] = true;
					break;
				}
			}
		}
		REP(c,C){
			for(int r = R-1; r>=0; r--){
				if(b[r][c] != '.'){
					if(b[r][c] == 'v')
						error=true;
					break;
				}
			}
		}
		cout << "Case #"<<tc<<": ";
		if(error)
			cout << "IMPOSSIBLE\n";
		else{
			int count=0;
			REP(r,R) REP(c,C)
				if(m[r][c]) count++;
			cout << count<<"\n";
}
}

return 0;
}


