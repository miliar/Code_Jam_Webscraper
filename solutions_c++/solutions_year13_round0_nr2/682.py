/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

using namespace std;

typedef long long LL;
typedef complex<double> point;
typedef long double ldb;
typedef pair<int,int> pii;

int n,m;
int row[1000],col[1000];
int a[1000][1000];

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		int n,m; cin >> n >> m;
		for (int i=0; i<n; i++) row[i]=0;
		for (int i=0; i<m; i++) col[i]=0;
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++){
				cin >> a[i][j];
				row[i] = max(row[i], a[i][j]);
				col[j] = max(col[j], a[i][j]);
			}
		bool bad = false;
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) if (a[i][j]!=row[i] && a[i][j]!=col[j])
				bad = true;
		cout << ((bad) ? ("NO") : ("YES")) << endl;
	}
	return 0;
}
