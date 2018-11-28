#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
#define dbg(args...) {debug,args; cerr << endl;}

#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define P1(a) (a).first
#define P2(a) (a).second
#define T1(a) (a).first
#define T2(a) (a).second.first
#define T3(a) (a).second.second
#define INF 1e20
#define EPS 1e-8

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, pii> tiii;

class debu {
	public:
	template<class someClass>
	debu & operator,(someClass arg) {
		cerr << arg << " ";
		return *this;
	}
} debug;


void init() {
	cout << setprecision(8) << fixed;
}

void solve(int testnr) {
	int row, res = 0;
	string str = "";
	vector<int> line1 (4, 0), line2 (4, 0);
	vector<int> garbage (4, 0);
	cin >> row;
	for (int i = 0; i < row; i++)
		for (int j = 0; j < 4; j++)
			cin >> line1[j];
	for (int i = row; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> garbage[j];
	cin >> row;
	for (int i = 0; i < row; i++)
		for (int j = 0; j < 4; j++)
			cin >> line2[j];
	for (int i = row; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> garbage[j];
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (line1[i] == line2[j]) {
				if (res == 0) res = line1[i];
				else str = "Bad magician!";
			}
	if (str.length() == 0) {
		if (res == 0) cout << "Volunteer cheated!" << endl;
		else cout << res << endl;
	} else cout << str << endl;
	return;
}

int main() {

	init();
    
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
	}
	return 0;
}
