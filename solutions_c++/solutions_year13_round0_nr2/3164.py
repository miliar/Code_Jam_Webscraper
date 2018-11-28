//#include <fstream> 
#include <iostream> 
#include <string> 
#include <list> 
#include <stack>
#include <sstream> 
#include <vector> 
#include <algorithm> 
#include <iomanip> 
#include <cmath>
#include <cstdio>
#include <map>
#include <queue>
#include <deque>
#include <set>
using namespace std;
 
int n, m, ans, p, k;
vector <int> stroka, stolb;
vector <vector <int> > a;

void check (int te) {
	cout << "Case #" << te << ": ";
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (a[i][j] != stolb[j] && a[i][j] != stroka[i]) {
				cout << "NO\n";
				return;
			}
		}
	}
	cout << "YES\n";
}

int main () {
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    //freopen("algo2.in", "r", stdin);freopen("algo2.out", "w", stdout);
	cin >> p;
	a.resize(120, vector <int> (120));
	for (int k = 1; k <= p; k++) {
		cin >> n >> m;
		//a.resize(n + 1, vector <int> (m + 1));
		stroka.resize(120);
		stolb.resize(120);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				cin >> a[i][j];
				stroka[i] = max(stroka[i], a[i][j]);
				stolb[j] = max(stolb[j], a[i][j]);
			}
		}
		check(k);
		for (int i = 1; i <= max(n, m); i++) {
			stroka[i] = 0;
			stolb[i] = 0;
		}
	}

    return 0;
}