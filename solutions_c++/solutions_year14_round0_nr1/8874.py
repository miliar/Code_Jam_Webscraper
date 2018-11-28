#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 0

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}
const int size = 4;

int row[2];
int ar[2][size][size];

int solution(int nTest) {
	For(it, 0, 2) {
		scanf("%d", &row[it]);
		row[it]--;
		For(i, 0, size) {
			For(j, 0, size) {
				scanf("%d", &ar[it][i][j]);
			}
		}
	}
	set<int> s;
	For(j, 0, size) {
		s.insert(ar[0][row[0]][j]);
	}
	int cnt = 0;
	int res = 0;
	For(j, 0, size) {
		int el = ar[1][row[1]][j];
		if(s.count(el) != 0) {
			cnt++;
			res = el;
		}
	}
	if(cnt == 0) {
		puts("Volunteer cheated!");
	} else if(cnt == 1) {
		printf("%d\n", res);
	} else {
		puts("Bad magician!");
	}

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
