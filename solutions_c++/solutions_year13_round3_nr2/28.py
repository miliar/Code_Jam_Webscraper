#include <cstdio>
#include <cstring>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++);
#define foreach(it,v) for (__typeof((v).end()) it = (v).begin(); it != (v).end(); it++)
typedef pair <int,int> PII;
int Tc;
map < PII, string > pool, res;

void ext(int x, int y, const string &s, char c) {
	res[PII(x, y)] = s + c;
}

void gao(int x, int y) {
	pool.clear();
	pool[PII(0, 0)] = "";
	int step = 1;
	while (!pool.count(PII(x, y))) {
		res.clear();
		foreach (it, pool) {
			int x = it->first.first;
			int y = it->first.second;
			const string &s = it->second;
			ext(x - step, y, s, 'W');
			ext(x + step, y, s, 'E');
			ext(x, y - step, s, 'S');
			ext(x, y + step, s, 'N');
		}
		step++;
		pool = res;
	}
	cout << pool[PII(x, y)] << endl;
}

int main() {
	scanf("%d", &Tc); 
	for (int ri = 0; ri < Tc; ri++) {
		printf("Case #%d: ", ri + 1);
		int x, y;
		scanf("%d%d", &x, &y);
		gao(x, y);
	}
	return 0;
}
