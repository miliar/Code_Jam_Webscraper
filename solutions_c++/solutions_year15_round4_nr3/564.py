#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <sstream>
#include <map>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define fi first
#define se second
#define sr(x) (int)x.size()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; For(_,a,b) cout << x[_] << ' '; cout << endl;}
#define Bit(s,i) (((s)&(1<<(i)))>0)
#define Two(x) (1<<(x))
const int MOD = 1000000007;
const int nmax = 1000000;
const double E = 1e-8;
const double PI = acos(-1);
typedef long long LL;
typedef pair<int,int> pii;
int n,m,stest;
string s,x;
map<string,int> F;
vector<int> st[nmax];
int res;
int Count[nmax];
int c[nmax][2];

void Cal(int u, int cur) {
	if ( cur > res ) return;
	if ( u > n ) {
		res = cur;
		return;
	}
	vector<int> rCount;
	vector<pii> rC;
	int rCur = cur;

	// remember
	For(i,0,sr(st[u])-1) {
		int x = st[u][i];
		rCount.push_back(Count[x]);
		rC.push_back(pii(c[x][0],c[x][1]));
	}

	// assign 0
	For(i,0,sr(st[u])-1) {
		int x = st[u][i];
		c[x][0] = true;
		if ( !Count[x] && c[x][0] && x[c][1] ) {
			cur++;
			Count[x] = true;
		}
	}
	Cal(u+1, cur);

	// restore
	For(i,0,sr(st[u])-1) {
		int x = st[u][i];
		Count[x] = rCount[i];
		c[x][0] = rC[i].fi;
		c[x][1] = rC[i].se;
	}
	cur = rCur;

	// assign 1
	For(i,0,sr(st[u])-1) {
		int x = st[u][i];
		c[x][1] = true;
		if ( !Count[x] && c[x][0] && x[c][1] ) {
			cur++;
			Count[x] = true;
		}
	}
	Cal(u+1, cur);

	// restore
	For(i,0,sr(st[u])-1) {
		int x = st[u][i];
		Count[x] = rCount[i];
		c[x][0] = rC[i].fi;
		c[x][1] = rC[i].se;
	}
	cur = rCur;

}

int main() {
	freopen("input.txt","r",stdin);
	cin >> stest;
	For(test,1,stest) {
		F.clear();
		m = 0;
		cin >> n;
		getline(cin, s);
		For(i,1,n) {
			getline(cin, s);
			st[i].clear();
			istringstream is(s);
			while ( is >> x ) {
				if ( F.find(x) == F.end() ) 
					F[x] = ++m;
				st[i].push_back(F[x]);
			}
		}
		For(i,1,m) c[i][0] = c[i][1] = false;


		For(i,0,sr(st[1])-1) c[st[1][i]] [0] = true;
		For(i,0,sr(st[2])-1) c[st[2][i]] [1] = true;
		

		res = m;
		int cur = 0;

		For(i,1,m) if ( c[i][0] && c[i][1] ) {
			cur++;
			Count[i] = true;
		} 
		else Count[i] = false;


		//BUG(cur);

		Cal( 3, cur );
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}