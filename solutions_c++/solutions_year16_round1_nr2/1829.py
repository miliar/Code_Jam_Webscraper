/*
Author:
Prob:
Link:
Tag:
Comp:
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define iii pair<ii, int>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ep emplace_back
#define sz(a) (int) a.size()
#define cl(a) a.clear()

#define vi vector<int>
#define vii vector<ii>

#define FOR(x,a,b) for (int x=a;x<=b;x++)
#define FOD(x,a,b) for (int x=a;x>=b;x--)
#define REP(x,a,b) for (int x=a;x<b;x++)
#define RED(x,a,b) for (int x=a;x>b;x--)

const int MAX = 1e5 + 10;
const int MAXN = 1e4 + 10;
const int MOD = 1e9 + 7;
const int inf = 1e9;
const double pi = acos(-1.0);
const double eps = 1e-6;

vector<int> a[110], f;
int b[110][110];
int mark[10000];
int t, n;

bool cmp(vector<int> a, vector<int> b){
	for (int i = 0; i < a.size(); i++)
		if (a[i] > b[i])
			return 0;
		else
			if (a[i] < b[i])
				return 1;
	return 1;
}

int Try(int m){
	int cnt = 0;
	for (int i = 0; i < 2*n-1; i++)
		if (m & (1 << i)){
			for (int j = 0; j < n; j++)
				b[cnt][j] = a[i][j];
			cnt++;
		}

	int flag, flagg;
	cnt = 0;
	flag = -1;
	for (int i = 0; i < 2*n-1; i++)
		if ((m & (1 << i)) == 0){
			flagg = 1;
			for (int j = 0; j < n; j++)
				if (b[j][cnt] != a[i][j]){
					flagg = 0;
					break;
				}
			// if (m == 22)
			// 	cout << "@#@!#!# " << flagg << "\n";
			if (!flagg){
				if (flag != -1) return 0;
				i--;
				flag = cnt;
			}
			cnt++;
		}
	f.resize(n);
	flag = (flag == -1 ? n-1 : flag);
	for (int i = 0; i < n; i++)
		f[i] = b[i][flag];
	return 1;
}

void process(){
	// if (a[0][0] != a[1][0]){
	// 	processFirst();
	// 	return;
	// }
	// if (a[2*n-2][n-1] != a[2*n-3][n-1]){
	// 	processLast();
	// 	return;
	// }
	// REP(i,0,n) b[0][i] = a[0][i];
	// REP(i,0,n) b[i][0] = a[1][i];
	// if ()
	for (int i = (1 << n)-1; i < (1 << (2*n)); i++)
		if (__builtin_popcount(i) == n){
			// cout << "## " << i << "\n";
			if (Try(i)){
				for (int i = 0; i < n; i++)
					cout << " " << f[i];
				cout << "\n";
				return;
			}
		}
}

int main(){
	// freopen("test.in", "rt", stdin);
	// freopen("test.ou", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	ios::sync_with_stdio(false);

	cin >> t;

	int x;
	FOR(cs,1,t){
		memset(mark, 0, sizeof(mark));
		cout << "Case #" << cs << ":";
		cin >> n;
		REP(i,0,2*n-1){
			REP(j,0,n){
				cin >> x;
				mark[x]++;
			}
		}
		x = 0;
		for (int i = 0; ; i++)
			if (mark[i] & 1){
				cout << " " << i;
				x++;
				if (x == n) break;
			}
		cout << "\n";
		// REP(i,0,2*n-1){
		// 	a[i].resize(n);
		// 	REP(j,0,n)
		// 		cin >> a[i][j];
		// }

		// vector<int> c;
		// sort(a, a+2*n-1, cmp);
		// // cout << cmp(a[5], a[7]) << "\n";
		// // return 0;
		// // cout << n << endl;
		// // for (int i = 0; i < 2*n-1; i++)
		// // 	for (int j = i+1; j < 2*n-1; j++)
		// // 		if (!cmp(a[i], a[j])){
		// // 			c = a[i];
		// // 			a[i] = a[j];
		// // 			a[j] = c;
		// // 		}
		// // REP(i,0,2*n-1){
		// // 	REP(j,0,n)
		// // 		cout << a[i][j] << " ";
		// // 	cout << "\n";
		// // }
		// // return 0;
		// process();
	}

	return 0;
}