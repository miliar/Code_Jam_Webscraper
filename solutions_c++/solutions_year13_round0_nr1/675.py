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

char mat[10][10];

bool check (char a, char b, char c, char d){
	string s = "";
	s+= a;
	s+= b;
	s+= c;
	s+= d;
	if (s.find('.') != s.npos) return false;
	if (s.find('X') != s.npos && s.find('O') != s.npos) return false;
	if (s.find('X') != s.npos) cout << "X won" << endl;
	if (s.find('O') != s.npos) cout << "O won" << endl;
	return true;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> mat[i][j];
		bool f = false;
		for (int i=0; i<4; i++) if (check(mat[i][0], mat[i][1], mat[i][2], mat[i][3])) { f = true; break; } if (f) continue;
		for (int i=0; i<4; i++) if (check(mat[0][i], mat[1][i], mat[2][i], mat[3][i])) { f = true; break; } if (f) continue;
		if (check(mat[0][0], mat[1][1], mat[2][2], mat[3][3])) continue;
		if (check(mat[0][3], mat[1][2], mat[2][1], mat[3][0])) continue;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++) if (mat[i][j]=='.'){
				cout << "Game has not completed" << endl;
				i=j=4;
				f=true;
			}
		if (f) continue;
		cout << "Draw" << endl;
	}
	return 0;
}
