#include <cassert>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <limits>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <map>
#include <bitset>
#include <deque>
#include <queue>
#include <forward_list>
#include <stack>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <utility>
#include <sstream>

using namespace std;
typedef unsigned long long int ulint;
typedef long long int lint;
typedef pair<int,int> pi;
typedef pair<lint,lint> pl;
typedef vector<int> vi;
struct dbg_ {
	template<typename T> dbg_ & operator ,(const T & x) {
		cout << x << ' ';
		return *this;
	}
} dbg_t;

#define EPS 0.0000001
#define REP(i,a,b) for(int i=a;i<b;i++)
#define PER(i,a,b) for(int i=a;i>b;i--)
#define REPi(type,cont,a) for (type<int>::iterator a = cont.begin(); a!=cont.end(); ++a)
#define REPs(cont,a) for (set<int>::iterator a = cont.begin(); a!=cont.end(); ++a)
#define ABS(x) ((x)<0?-(x):(x))
#define FABS(x) ((x)+eps<0?-(x):(x))
#define MIN(X, Y)  ((X) < (Y) ? (X) : (Y))
#define MAX(X, Y)  ((X) > (Y) ? (X) : (Y))
#define NUMDIGIT(x,y) (((int)(log10((x))/log10((y))))+1)
#define MP make_pair
#define PB push_back
#define ALL(a) a.begin(), a.end()
#define HAS(a,b) (a.find(b) != a.end())
#define x first
#define y second
#ifdef SLONICHOBOT
	#undef dbg
	#undef tu
	#define tu cout << "#line: " << __LINE__ << endl
	#define dbg(args ...) { cout << "|" << __LINE__ << "| "; dbg_t,args;cout << endl; }
	#define dbgg(X) cerr << #X ": " << X << endl
#else
	#define tu
	#define dbg
	#define dbgg
#endif

int grid[51][51];
int n; 
vector<vector<int>> data;
bool used[51][2];

bool doit(int pos) {
	// dbg(pos, 2*n-1);
	if (pos == 2*n-1) return true;
	// radek
	REP(i,0,n) {
		bool ok = true; int last=n;
		if (used[i][0]) continue;
		REP(j,0,n) {
			if (grid[i][j] != 0 && grid[i][j] != data[pos][j]) { ok = false; break; }
			if (grid[i][j] == 0) { last=j; break; }
		}
		if (ok) {
			used[i][0] = 1;
			REP(j,0,n) {
				grid[i][j] = data[pos][j];
			}
			if(doit(pos+1)) return true;
			used[i][0] = 0;
		}
		REP(j,last,n) {
			grid[i][j] = 0;
		}
		if (ok) break;
	}
	// sloupec
	REP(i,0,n) {
		bool ok = true; int last=n;
		if (used[i][1]) continue;
		REP(j,0,n) {
			if (grid[j][i] != 0 && grid[j][i] != data[pos][j]) { ok = false; break; }
			if (grid[j][i] == 0) { last=j; break; }
		}
		if (ok) {
			used[i][1] = 1;
			REP(j,0,n) {
				grid[j][i] = data[pos][j];
			}
			if (doit(pos+1)) return true;
			used[i][1] = 0;
		}
		REP(j,last,n) {
			grid[j][i] = 0;
		}
		if (ok) break;
	}
	return false;
}

void solve() {
	memset(grid,0,sizeof(grid));
	memset(used,0,sizeof(used));
	data.clear();
	cin >> n;
	REP(i,0,2*n-1) {
		vector<int> x;
		REP(j,0,n) {
			int a; cin >> a;
			x.PB(a);
		}
		data.PB(x);
	}
	sort(ALL(data), [](const vector<int> & a, const vector<int> &b){ return a[0] < b[0]; });
	doit(0);

	cout << endl;
	REP(i,0,n) {
		REP(j,0,n) {
			cout << grid[i][j] << '\t';
		}
		cout << endl;
	}
	REP(i,0,n) {
		if (!used[i][0]) {
			REP(j,0,n)
				cout << grid[i][j] << ' ';
			cout << endl;
			return ;
		}
		if (!used[i][1]) {
			REP(j,0,n)
				cout << grid[j][i] << ' ';
			cout << endl;
			return ;
		}
		
	}
	
}

int main()
{
	int T; cin >> T;
	REP(i,0,T) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}

	return 0;
}
