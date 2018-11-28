/*
ID: oooctav1
PROG: checker
LANG: C++
*/
#include <iostream> 
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <stack>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define N 100005

int a[101][101];

int main() {
//	freopen ("checker.out","w",stdout);
//	freopen ("checker.in","r",stdin);
	ios_base::sync_with_stdio(false);

	/*
	int t;
	cin >> t;
	string s;
  getline(cin, s);
	for (int tt = 1; tt <= t; tt++) {
		string s;
		getline(cin, s);

		cout << "Case #" << tt << ": " << rez << endl; 
	}
		*/

	int t;
	cin >> t;
	string s;
  getline(cin, s);
	for (int tt = 1; tt <= t; tt++) {
		int n,m;
		cin >> n >> m;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				cin >> a[i][j];

		string ans = "YES";
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				bool line = true, col = true;
				for (int k = 1; k <= n; k++)
					if (a[i][j] < a[k][j]) {line = false; break;}
				for (int k = 1; k <= m; k++)
					if (a[i][j] < a[i][k]) {col = false; break;}
				if (!line && !col) { ans = "NO"; break;} 
			}
		}

		cout << "Case #" << tt << ": " << ans << endl; 
	}

	return 0;
}
