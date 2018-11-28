#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <unordered_map>
#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

const int dr[] = {0, 1, 0, -1};
const int dc[] = {1, 0, -1, 0};

int R, C, T;
vector < VI > table;
int BT_ans;

inline bool valid(const int &a, const int &b){
	return a >= 0 && b >= 0 && a < R && b < C;
}

inline int cost(int r, int c){
	int ans = 0;
	FOR(mv,0,4) if(valid(r+dr[mv],c+dc[mv]) && table[r+dr[mv]][c+dc[mv]])
		ans++;
	return ans;
}

void BT(int r, int c){
	if(r == R){
		if(T)
			return;
		int bad = 0;
		FOR(i,0,R) FOR(j,0,C) if(table[i][j])
			bad += cost(i,j);
		BT_ans = min(BT_ans, bad/2);
		return;
	}
	int nr = (c == C-1) ? r+1 : r;
	int nc = (c == C-1) ? 0 : c+1;
	BT(nr,nc);
	table[r][c] = 1;
	T--;
	BT(nr,nc);
	table[r][c] = 0;
	T++;
}

int main(){
	ios_base::sync_with_stdio(false);

	int Tsts;
	cin >> Tsts;
	FOR(cnt,0,Tsts){
		cin >> R >> C >> T;
		table.resize(R);
		FOR(r,0,R)
			table[r] = VI(C);

		BT_ans = 1<<30;
		BT(0,0);

		cout << "Case #" << cnt+1 << ": " << BT_ans << endl;
	}

	return 0;
}
