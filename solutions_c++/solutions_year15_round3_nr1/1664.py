#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(i,c)  for(auto i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++)
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

//#include "cout11.h"

int R,C,W;
int P;

vector<int> st;

int sub(int h, int pc) {
//	cout << "sub" << st << " " << h << " " << pc << endl;

	int dy = -1, dn = -1;
	for (int i=0; i<C; ++i) {
		if (st[i] == 1) {
			if (dy >= 0 && dn >= 0 && dy < dn) return -1;
			dy = i;
		} else if (st[i] == -1) {
			dn = i;
		}
	}

	if (h == W) {
		int k = 0;
		for (int j=0; j<C-1; ++j) {
			if (st[j]>0 && st[j+1]>0) ++k;
		}
		if (k == W-1) return pc;
		return -1;
	}
	if (C-pc < W-h) return -1;

	int res = C+1;
	for (int i=0; i<C; ++i) {
		if (st[i] != 0) continue;

		st[i] = 1;
		int u1 = sub(h+1, pc+1);
		st[i] = -1;
		int u2 = sub(h, pc+1);
		st[i] = 0;

		int u = max(u1,u2);
		if (u < 0) continue;

		res = min(res, u);
	}

	if (res == C+1) return -1;
	return res;
}

int main()
{
  int _T; cin >> _T; // 55 | 1-100
  for (int _t=1; _t<=_T; ++_t) {
    cin >> R >> C >> W; // 1, 1-10, 1-C
    P = 1 << C;

    st.resize(C, 0);
    cout << "Case #" << _t << ": " << sub(0, 0) << endl;
  }
}
