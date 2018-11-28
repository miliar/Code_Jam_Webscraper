#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

int chd[3200005][2];
int val[3200005];
string a[100005];
int cnt = 1;

void insert (string s, int id){
	int now = 0;
	FOR (i, 0, SIZE (s)-1){
		if (!chd[now][s[i] - '0']){
			chd[now][s[i] - '0'] = cnt ++;
		}
		now = chd[now][s[i] - '0'];
	}
	if (!val[now]){
		val[now] = id;
	}
}

bool query (string s){
	int now = 0, ans = 150000;
	if (val[now]){
		ans = val[now];
	}
	FOR (i, 0, SIZE (s)-1){
		if (!chd[now][s[i] - '0']){
			break;
		}
		now = chd[now][s[i] - '0'];
		if (val[now] && val[now] < ans){
			ans = val[now];
		}
	}
	if (ans  == 150000){
		return 1;
	}
	return a[ans] == "allow";
}

int main (){
	int n, m;
	cin >> n >> m;
	FOR (i, 1, n){
		string s;
		cin >> a[i] >> s;
		stringstream ss(s + '.');
		vector<int> vec;
		int t;
		char c;
		while (ss >> t >> c){
			vec.PB (t);
		}
		ll x = 0;
		FOR (j, 0, 3){
			x = (x << 8) + vec[j];
		}
		int ttt = 32;
		if (SIZE (vec) > 4){
			x >>= (32-vec[4]);
			ttt = vec[4];
		}
		string sx;
		while (ttt--){
			sx += (char)((x&1) + '0');
			x >>= 1;
		}
		reverse (ALL (sx));
		insert (sx, i);
	}
	FOR (i, 1, m){
		string s;
		cin >> s;
		stringstream ss(s + '.');
		vector<int> vec;
		int t;
		char c;
		while (ss >> t >> c){
			vec.PB (t);
		}
		ll x = 0;
		FOR (j, 0, 3){
			x = (x << 8) + vec[j];
		}
		string sx;
		int ttt = 32;
		while (ttt--){
			sx += (char)((x&1) + '0');
			x >>= 1;
		}
		reverse (ALL (sx));
		cout << (query (sx) ? "YES" : "NO") << endl;
	}
}

