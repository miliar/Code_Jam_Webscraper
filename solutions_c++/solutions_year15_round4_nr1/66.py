
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <fstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

string field[128];
int ids[128][128];

int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, 1, 0, -1};
void calc(){
	map<char, int> dir;
	dir['^'] = 2;
	dir['<'] = 3;
	dir['>'] = 1;
	dir['v'] = 0;
	int R, C;
	cin >> R >> C;
	FOR(r,0,R)cin >> field[r];
	int ID = 0;
	FOR(r,0,R){
		FOR(c,0,C){
			if(field[r][c] == '.')ids[r][c] = -1;
			else ids[r][c] = ID++;
		}
	}
	int res = 0;
	FOR(r,0,R)FOR(c,0,C){
		if(ids[r][c] != -1){
			int d = dir[field[r][c]];
			int rr = r + dr[d], cc = c + dc[d];
			bool found = false;
			while(rr >= 0 && rr < R && cc >= 0 && cc < C){
				if(ids[rr][cc] != -1){
					found = true;
					break;
				}
				rr = rr + dr[d], cc = cc + dc[d];
			}
			if(found)continue;
			for(d = 0; d < 4 && ! found; d++){
				rr = r + dr[d], cc = c + dc[d];
				while(rr >= 0 && rr < R && cc >= 0 && cc < C){
					if(ids[rr][cc] != -1){
						found = true;
						break;
					}
					rr = rr + dr[d], cc = cc + dc[d];
				}
			}
			if(!found){
				cout << "IMPOSSIBLE\n";
				return;
			}
			res++;
		}
	}
	cout << res << endl;
}

int main() {
	int TC;
	cin >> TC;
	FOR(tc,1,TC+1){
		cout << "Case #" << tc << ": ";
		calc();
	}
	return 0;
}
