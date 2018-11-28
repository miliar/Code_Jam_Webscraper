#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL; 
typedef pair<int, int> PII;
typedef vector<int> VI;
#define PB push_back
#define MP make_pair
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for(int i = (a); i <= (b); i++)
#define CLR(x, a) memset(x, a, sizeof(x))
//#define L(x) ((x) << 1)
#define R(x) (((x) << 1) + 1)
#define LB(x) ((x)&(-(x)))
#define SL(x) (1 << (x))
#define X first
#define Y second
const int MAXN = 100 + 20;


int main(){

	int T; cin >> T;
	FOR(cas, T){
		printf("Case #%d: ", cas + 1);
		set<int> dict;
		int r1, r2, cnt = 0, res;
		cin >> r1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0, tmp; j < 4; j++) {
				cin >> tmp;
				if (i == r1 - 1) {
					dict.insert(tmp);
				}
			}
		}
		cin >> r2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0, tmp; j < 4; j++) {
				cin >> tmp;
				if (i == r2 - 1) {
					if (dict.find(tmp) != dict.end()) {
						cnt++;
						res = tmp;
					}
				}
			}
		}
		if (cnt == 1) {
			cout << res << endl;
		} else if (cnt > 1) {
			cout << "Bad magician!" << endl;
		} else {
			cout << "Volunteer cheated!" << endl;
		}
	}
}