#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>
#include <cstring>

#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi >
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vpii vector<pii >
#define vb vector<bool>
#define min(x,y) (x < y ? x : y)
#define min3(x,y,z) (min(x,min(y,z)))
#define max(x,y) (x > y ? x : y)
#define max3(x,y,z) (max(x,max(y,z)))
#define forn(i,n) for(int i = 0;i < n;i++)
#define sqrt(x) (pow(x,0.5))
#define sqr(x) (x * x)
#define mp make_pair
#define STDFILE 1
#define TASKNAME "xx"

const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;
const ld eps = 1e-9;

using namespace std;

const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, 1, -1, -1, 0, 1};

int st[6];
bool ans[6][6], used[6][6], good[6][6];
int n, m, bomb;
bool okey;

bool check() {
	for (int i = 0; i < 6; i++)
		for (int j = 0; j < 6; j++) {
			used[i][j] = false;
			good[i][j] = false;
		}

		int cnt = 0;
		for (int i = 0; i < n; i++) {
			cnt += st[i];
			for (int j = 0; j < st[i]; j++) {
				good[i][j] = true;
				used[i][j] = true;
			}
		}

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!used[i][j]) {
					bool ok = false;
					for (int k = 0; k < 8; k++)
						if (used[i + dx[k]][j + dy[k]]) ok = true;
					if (ok) {
						good[i][j] = true;
						cnt++;
					}
				}
				if (cnt == n * m - bomb) {
					for (int i = 0; i < n; i++)
						for (int j = 0; j < m; j++) ans[i][j] = good[i][j];
					return true;
				}
				return false;
}

void rec(int len) {
	if (okey) return;
	if (len == n - 1) {
		if (check()) okey = true;
		return;
	}
	for (int i = (len == 0) ? 1 : 0; i < m; i++) {
		st[len] = i;
		rec(len + 1);
		st[len] = 0;
	}
}

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	int t;
	cin >> t;
	forn(i,t){
		cout << "Case #" << (i + 1) << ": " << endl;
		cin >> n >> m >> bomb;
		for (int i = 0; i < 6; i++)
			for (int j = 0; j < 6; j++) ans[i][j] = false;
	    for (int i = 0; i < 6; i++) st[i] = 0;
		if (bomb == n * m - 1) {
			for (int k = 0; k < n; k++) {
				for (int j = 0; j < m; j++)
					if (k == 0 && j == 0) cout << 'c';
					else cout << '*';
				cout << endl;
			}
			continue;
		}
		if (n == 1) {
			for (int k = 0; k < n * m - bomb; k++) ans[0][k] = true;
			for (int k = 0; k < n; k++) {
				for (int j = 0; j < m; j++) {
					if (k == 0 && j == 0) {
						cout << 'c';
						continue;
					}
					if (ans[k][j]) cout << '.';
					else cout << '*';
				}
				cout << endl;
			}
			continue;
		}
		if (m == 1) {
			for (int k = 0; k < n * m - bomb; k++) ans[k][0] = true;
			for (int k = 0; k < n; k++) {
				for (int j = 0; j < m; j++) {
					if (k == 0 && j == 0) {
						cout << 'c';
						continue;
					}
					if (ans[k][j]) cout << '.';
					else cout << '*';
				}
				cout << endl;
			}
			continue;
		}
		okey = false;
		rec(0);
		if (!okey) {
			cout << "Impossible" << endl;
			continue;
		}
		for (int k = 0; k < n; k++) {
			for (int j = 0; j < m; j++) {
				if (k == 0 && j == 0) {
					cout << 'c';
					continue;
				}
				if (ans[k][j]) cout << '.';
				else cout << '*';
			}
			cout << endl;
		}
	}
	return 0;
}