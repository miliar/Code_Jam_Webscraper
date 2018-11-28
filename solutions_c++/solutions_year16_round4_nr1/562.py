#include <bits/stdc++.h>
using namespace std;
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii, ii>
#define vvi vector<vi>
#define MAXN 105
#define MAXE 10005
#define FOR(x,n) for(int x = 0; x < n; x++)
#define FOR1e(x,n) for(int x = 1; x <= n; x++)
#define MOD 1000000007

	int n, t, r, p, s, players, mr, mp, ms;
char order[100005], copia[100005], c1[100005], c2[100005];
bool check(char l) {
		int players = (1 << n);
		order[0] = l;

		mr = 0; mp = 0; ms = 0;
		if(l == 'R') mr++;
		if(l == 'S') ms++;
		if(l == 'P') mp++;
		FOR(x, n) {
			FOR(y, (1 << x)) {
				if(order[y] == 'R') {
					copia[2*y] = 'R';
					copia[2*y+1] = 'S';
					ms++;
				}

				if(order[y] == 'S') {
					copia[2*y] = 'P';
					copia[2*y+1] = 'S';
					mp++;
				}

				if(order[y] == 'P') {
					copia[2*y] = 'P';
					copia[2*y+1] = 'R';
					mr++;
				}
			}
			FOR(y, (1 << x+1)) {
				order[y] = copia[y];
			}
			order[(1<< x+1)] = '\0';
	//		printf("%s %d %d %d\n", order, mr, mp, ms);
			if(mr > r || mp > p || ms > s) return false;
		}
		FOR(block, n) {
			int start = 0;
			while(start < (1 << n)) {
				FOR(tmp, (1 << block)) {
					c1[tmp] = order[start + tmp];
					c2[tmp] = order[start + tmp + (1 << block)];
				}
				c1[(1 << block)] = '\0';
				c2[(1 << block)] = '\0';
				if(strcmp(c1, c2) < 0) {
					FOR(tmp, (1 << block)) {
						order[start + tmp] = c1[tmp];
						order[start + tmp + (1 << block)] = c2[tmp];
					}
				}
				else {
					FOR(tmp, (1 << block)) {
						order[start + tmp] = c2[tmp];
						order[start + tmp + (1 << block)] = c1[tmp];
					}	
				}
				start += 2*(1 << block);
				//printf("%d %s %s\n", start, c1, c2);
				
			}
		}
		order[players] = '\0';

		if(mr == r && mp == p && ms == s) return true;
		return false;
}
int main() {
	scanf("%d", &t);
	FOR1e(caso, t) {
		scanf("%d %d %d %d", &n, &r, &p, &s);
		if(check('R') || check('S') || check('P')) printf("Case #%d: %s\n", caso, order);
		else printf("Case #%d: IMPOSSIBLE\n", caso);
	}
	return 0;
}