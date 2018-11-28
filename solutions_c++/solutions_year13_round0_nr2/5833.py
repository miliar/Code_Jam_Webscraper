#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <deque>
using namespace std;
#ifdef _DEBUG
#include <fstream>
ifstream cin ("input.txt");
ofstream cout ("output.txt");
#else
#include <fstream>
ifstream cin ("segment.in");
ofstream cout ("segment.out");                                                                                                
#endif
int n, m, i, j, t, mn[102], mm[102], a[102][102];

bool checking(){
	for ( int i = 0; i < n; i++ ){
		for ( int j = 0; j < m; j++ ){
			if ( a[i][j] != mn[i] && a[i][j] != mm[j] ) return 0;
		}
	}
	return 1;
}

int main () {
	cin >> t;
	for ( int l = 0; l < t; l++ ){
		cin >> n >> m;
		for ( i = 0; i < n; i++ ){
			for ( j = 0; j < m; j++ ){
				cin >> a[i][j];
				if ( mm[j] < a[i][j] ) mm[j] = a[i][j];
				if ( mn[i] < a[i][j] ) mn[i] = a[i][j];
			}
		}
		cout << "Case #" << l + 1 << ": ";
		if ( checking() == 0 ) {
			cout << "NO\n";
		}else{
			cout << "YES\n";
		}
		for ( i = 0; i < n; i++ ) mn[i] = 0;
		for ( j = 0; j < m; j++ ) mm[j] = 0;
	}
}
