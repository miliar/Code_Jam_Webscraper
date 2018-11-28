//be name oo
#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <set>
#include <complex>
#include <iomanip>
#include <queue>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define show(x) cerr << "#" << #x << ": " << x << endl
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> pii;
typedef complex<double> point;

const int MAX_N = 100 + 10;

int tab[MAX_N][MAX_N];
int max_row[MAX_N];
int max_col[MAX_N];

int main(){
	int testCount;
	cin >> testCount;
	for(int testNumber = 1; testNumber <= testCount; testNumber++){
		cout << "Case #" << testNumber << ": ";
		int n, m;
		cin >> n >> m;
		memset(max_row, 0, sizeof max_row);
		memset(max_col, 0, sizeof max_col);
		FOR(i, n)
			FOR(j, m){
				cin >> tab[i][j];
				max_row[i] = max(max_row[i], tab[i][j]);
				max_col[j] = max(max_col[j], tab[i][j]);
			}
		bool can = true;
		FOR(i, n)
			FOR(j, m)
				if(tab[i][j] != max_row[i] && tab[i][j] != max_col[j])
					can = false;
		if(can)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}


