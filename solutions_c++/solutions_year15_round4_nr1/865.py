#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#define PB push_back
#define FI first
#define SE second
#define MP make_pair

using namespace std;

typedef int LL;
typedef pair<LL, LL> pi;

LL tab[101][101];
LL visited[101][101];

LL result = 0;

LL R, C;
LL cols[101];
LL rows[101];

vector<pi> points;

int main () {
	int t;
	scanf("%d\n", &t);
	for(int i = 1; i <= t; ++i) {
		result = 0;
		char c;
		points.clear();
		LL cols[101];
		LL rows[101];
		for(int a = 0; a < 101; a++) {
			cols[a] = 0;
			rows[a] = 0;
		}

		for(int a = 0; a < 101; a++) {
			for(int b = 0; b < 101; b++) {
				tab[a][b] = 0;
			}
		}
		scanf("%d %d\n", &R, &C);
		for(int a = 0; a < R; ++a) {
			for(int b = 0; b < C; b++) {
				c = getchar();
				if(c != '.') { 
					rows[a]++;
					cols[b]++;
					int r = 0;
					tab[a][b] = 1;
					if(c == '^')
						r = 1;
					else if(c == '>')
						r = 2;
					else if(c == 'v')
						r = 3;
					else if(c == '<')
						r = 4;
					points.PB(MP(a * C + b, r));
				}
			}
			getchar();
		}
		int ok = 0;
		for(int a = 0; a < points.size(); ++a) {
			pi point = points[a];
			int c = point.FI % C;
			int r = point.FI / C;
			if(rows[r] == 1 && cols[c] == 1) {
				ok = 1;
				break;
			}	
		}

		if(ok == 1)
			printf("Case #%d: IMPOSSIBLE\n", i);
		else {
			LL result = 0;
			for(int a = 0; a < points.size(); ++a) {
				pi point = points[a];
				int c = point.FI % C;
				int r = point.FI / C;
				int ok = 0;
				switch(point.SE) {
					case 1:
						for(int b = r - 1; b >= 0; b--) {
							if(tab[b][c] == 1) {
								ok = 1;
								break;
							}
						}
						break;
					case 2:
						for(int b = c + 1; b < C; b++) {
							if(tab[r][b] == 1) {
								ok = 1;
								break;
							}
						}
						break;
					case 3:
						for(int b = r + 1; b < R; b++) {
							if(tab[b][c] == 1) {
								ok = 1;
								break;
							}
						}
						break;
					case 4:
						for(int b = c - 1; b >= 0; b--) {
							if(tab[r][b] == 1) {
								ok = 1;
								break;
							}
						}
						break;
				}
				result += 1 - ok;
			}	
			printf("Case #%d: %d\n", i,result);
		}
	}
	return 0;
}