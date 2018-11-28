#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int N = 100, H = 200, MAX_SHOT_PER_MONSTER = 10, MAX_SHOT = N * MAX_SHOT_PER_MONSTER, INF = (int) 1e9;
int myDamage, towerDamage, n, h[N + 1], point[N];
int f[H + 1][MAX_SHOT + 1][2], g[H + 1][MAX_SHOT + 1][2];

bool checkMax(int &a, int b) {
	return a < b ? a = b, true : false;
}

int main() {
	int testCount; cin >> testCount;
	for(int testID = 0; testID < testCount; ++testID) {
		cin >> myDamage >> towerDamage >> n;
		for(int i = 0; i < n; ++i) cin >> h[i] >> point[i]; h[n] = 0;
		memset(f, 0xc1, sizeof f);
		f[h[0]][0][0] = 0;
		for(int i = 0; i < n; ++i) {
			memset(g, 0xc1, sizeof g);
			for(int hp = h[i]; hp > 0; --hp)
				for(int keep = 0; keep <= MAX_SHOT; ++keep) {
					if(f[hp][keep][0] >= 0) {
						if(keep > 0) {
							if(hp <= myDamage) {
								checkMax(g[h[i + 1]][keep - 1][0], f[hp][keep][0] + point[i]);
							} else {
								checkMax(f[hp - myDamage][keep - 1][0], f[hp][keep][0]);
							}
						}
						if(keep < MAX_SHOT) checkMax(f[hp][keep + 1][1], f[hp][keep][0]);
						if(hp <= myDamage) {
							checkMax(g[h[i + 1]][keep][1], f[hp][keep][0] + point[i]);
						} else {
							checkMax(f[hp - myDamage][keep][1], f[hp][keep][0]);
						}
					}
					if(f[hp][keep][1] >= 0) {
						if(hp <= towerDamage) {
							checkMax(g[h[i + 1]][keep][0], f[hp][keep][1]);
						} else {
							checkMax(f[hp - towerDamage][keep][0], f[hp][keep][1]);
						}
					}
				}
			memcpy(f, g, sizeof f);
		}
		int res = 0;
		for(int keep = 0; keep <= MAX_SHOT; ++keep) {
			for(int turn = 0; turn < 2; ++turn) {
				checkMax(res, f[0][keep][turn]);
			}
		}
		printf("Case #%d: %d\n", testID + 1, res);
	}
	return 0;
}
