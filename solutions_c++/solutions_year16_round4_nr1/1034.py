#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>

#define mp(a, b) make_pair(a, b)
using namespace std;

typedef pair<pair<int, int>, int> trip;

trip tpd[4][13];
string prec[4][13];

const int PAPER = 0, ROCK = 1, SCISSOR = 2;

trip tree(int topo, int nivel) {
	if (tpd[topo][nivel].second != -1) {
		return tpd[topo][nivel];
	}
	
	trip left, right;
	
	if (nivel == 0) {
		if (topo == PAPER) {
			prec[topo][nivel] = "P";
			return mp(mp(1, 0), 0);
		} else if (topo == ROCK) {
			prec[topo][nivel] = "R";
			return mp(mp(0, 1), 0);
		} else {
			prec[topo][nivel] = "S";
			return mp(mp(0, 0), 1);
		}
	}
	
	switch (topo) {
		case PAPER:
			left = tree(PAPER, nivel - 1);
			right = tree(ROCK, nivel - 1);
			
			if (prec[PAPER][nivel - 1] < prec[ROCK][nivel - 1]) {
				prec[topo][nivel] = prec[PAPER][nivel - 1] + prec[ROCK][nivel - 1];
			} else {
				prec[topo][nivel] = prec[ROCK][nivel - 1] + prec[PAPER][nivel - 1];
			}
			
			break;
		case ROCK:
			left = tree(ROCK, nivel - 1);
			right = tree(SCISSOR, nivel - 1);
			
			if (prec[ROCK][nivel - 1] < prec[SCISSOR][nivel - 1]) {
				prec[topo][nivel] = prec[ROCK][nivel - 1] + prec[SCISSOR][nivel - 1];
			} else {
				prec[topo][nivel] = prec[SCISSOR][nivel - 1] + prec[ROCK][nivel - 1];
			}
			
			break;
		case SCISSOR:
			left = tree(PAPER, nivel - 1);
			right = tree(SCISSOR, nivel - 1);
			
			if (prec[PAPER][nivel - 1] < prec[SCISSOR][nivel - 1]) {
				prec[topo][nivel] = prec[PAPER][nivel - 1] + prec[SCISSOR][nivel - 1];
			} else {
				prec[topo][nivel] = prec[SCISSOR][nivel - 1] + prec[PAPER][nivel - 1];
			}
			
			break;
	}
	
	trip res;
	
	res.first.first = left.first.first + right.first.first;
	res.first.second = left.first.second + right.first.second;
	res.second = left.second + right.second;
	
	return res;
}

int main() {
	int T, N, R, P, S;
	
	scanf("%d", &T);
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 13; j++) {
			tpd[i][j].second = -1;
		}
	}
	
	for (int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		
		scanf("%d %d %d %d", &N, &R, &P, &S);
		trip exp = mp(mp(P, R), S);
		bool possible = false;
		
		for (int i = 0; (!possible) && (i < 4); i++) {
			if (tree(i, N) == exp) {
				printf("%s\n", prec[i][N].c_str());
				possible = true;
			}
		}
		
		if (!possible) {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}