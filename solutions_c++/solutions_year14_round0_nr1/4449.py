#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <algorithm>
#include <iostream>
#define infinity 2139062143
#define infinity64 9187201950435737471LL
#define foreach( i, n ) 	for(int (i) = 0; (i) < (n); ++(i))
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100
using namespace std;

int chosen[20];


int main () {
	int n, t, f, l, count, pivot;
	scanf("%d", &t);
	foreach (n, t) {
		memset(chosen, 0, sizeof chosen);
		foreach (k, 2) {
			scanf("%d", &f);
			foreach (i, 4) {
				foreach (j, 4) {
					scanf("%d", &l);
					if (i + 1 == f) {
						chosen[l]++;
					}
				}
			}
		}
		count = 0;
		for (int i = 1; i<=16; i++) {
			if (chosen[i] == 2) {
				count++;
				pivot = i;
			}
		}
		if (count == 0) {
			printf("Case #%d: Volunteer cheated!\n", n+1);
		} else if (count == 1) {
			printf("Case #%d: %d\n", n+1, pivot);
		} else {
			printf("Case #%d: Bad magician!\n", n+1);
		}
	}
	return 0;
}



