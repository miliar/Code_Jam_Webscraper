#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cmath>

using namespace std;

#define debug(a) cerr << #a << ": " << a << endl;
#define debugv(b) cerr << #b << ":\n"; for(int countvec = 0; countvec < b.size(); countvec++) {cerr << b[countvec] << "    ";} cerr << endl;
#define debugm(c) cerr << #c << ":\n"; for(int countmat = 0; countmat < c.size(); countmat++) {for(int countbb = 0; countbb < c[countmat].size(); countbb++) { cerr << c[countmat][countbb] << "    "; } cerr << endl; }
string tos(int a) {ostringstream os(""); os << a; return os.str();}


string board[4];

int main() {
	ios::sync_with_stdio(true);
	freopen("D:/input.txt","r",stdin);
	freopen("D:/output.txt","w",stdout);
	
	int n;
	scanf("%d\n", &n);
	for(int tc = 1; tc <= n; tc++) {
		bool cond = false;
		for(int i = 0; i < 4; ++i) getline(cin, board[i]);
		string line;
		getline(cin, line);
		for(int i = 0; i < 4; ++i) {
			int o = 0, x = 0, t = 0;
			for(int j = 0; j < 4; ++j) {
				if(board[i][j] == 'O') ++o;
				if(board[i][j] == 'X') ++x;
				if(board[i][j] == 'T') ++t;
			}
			if((o == 4) || (o == 3 && t == 1)) {
				printf("Case #%d: O won\n", tc);
				cond = true;
				break;
			}
			else if((x == 4) || (x == 3 && t == 1)) {
				printf("Case #%d: X won\n", tc);
				cond = true;
				break;
			}
		}
		if(cond) continue;
		for(int i = 0; i < 4; ++i) {
			int o = 0, x = 0, t = 0;
			for(int j = 0; j < 4; ++j) {
				if(board[j][i] == 'O') ++o;
				if(board[j][i] == 'X') ++x;
				if(board[j][i] == 'T') ++t;
			}
			if((o == 4) || (o == 3 && t == 1)) {
				printf("Case #%d: O won\n", tc);
				cond = true;
				break;
			}
			else if((x == 4) || (x == 3 && t == 1)) {
				printf("Case #%d: X won\n", tc);
				cond = true;
				break;
			}
		}
		if(cond) continue;
		
		int o = 0, x = 0, t = 0;
		for(int i = 0; i < 4; ++i) {
			if(board[i][i] == 'O') ++o;
			if(board[i][i] == 'X') ++x;
			if(board[i][i] == 'T') ++t;
		}		
		if((o == 4) || (o == 3 && t == 1)) {
			printf("Case #%d: O won\n", tc);
			continue;
		}
		else if((x == 4) || (x == 3 && t == 1)) {
			printf("Case #%d: X won\n", tc);
			continue;
		}
		
		o = 0, x = 0, t = 0;
		for(int i = 0; i < 4; ++i) {
			if(board[i][3 - i] == 'O') ++o;
			if(board[i][3 - i] == 'X') ++x;
			if(board[i][3 - i] == 'T') ++t;
		}
		
		if((o == 4) || (o == 3 && t == 1)) {
			printf("Case #%d: O won\n", tc);
			continue;
		}
		else if((x == 4) || (x == 3 && t == 1)) {
			printf("Case #%d: X won\n", tc);
			continue;
		}
		
		int empty = 0;
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j) if(board[i][j] == '.') ++empty;
		
		if(empty) printf("Case #%d: Game has not completed\n", tc);
		else printf("Case #%d: Draw\n", tc);
		
		
	}
	
	return 0;
}
