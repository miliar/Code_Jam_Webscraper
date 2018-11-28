#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp make_pair
#define pb push_back
 
int main() {
	int T;
	cin >> T;
	FOR(Z, 0, T) {
		char field[4][4];
		bool comp = true;
		cout << "Case #" << Z+1 << ": ";
		FOR(i, 0, 4)
			FOR(j, 0, 4) {
				cin >> field[i][j];
				if(field[i][j] == '.')
					comp = false;
			}
		cin.get();
		char won;
		for(auto X : {'X', 'O'}) {
			won = X;
			FOR(i, 0, 4) {
				bool ok = true;
				FOR(j, 0, 4) {
					if(field[i][j] != X && field[i][j] != 'T') {
						ok = false;
						break;
					}
				}
				if(ok)
					goto ne;
			}
			FOR(i, 0, 4) {
				bool ok = true;
				FOR(j, 0, 4) {
					if(field[j][i] != X && field[j][i] != 'T') {
						ok = false;
						break;
					}
				}
				if(ok)
					goto ne;
			}
			bool ok = true;
			FOR(i, 0, 4) {
				if(field[i][i] != X && field[i][i] != 'T') {
					ok = false;
					break;
				}
			}
			if(ok)
				goto ne;
			ok = true;
			FOR(i, 0, 4) {
				if(field[3-i][i] != X && field[3-i][i] != 'T') {
					ok = false;
					break;
				}
			}
			if(ok)
				goto ne;
		}
		if(comp)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
		continue;
ne:
		cout << won << " won" << endl;
		continue;
	}
	return 0;
}
