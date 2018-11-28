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
#define full 1001
using namespace std;

char str[full][full];
int pos[full], len[full], att[full];

int main () {
	int n, t, acc, act, med, ant;
	char car; bool merda;
	scanf(" %d", &t);
	foreach (it, t) {
		scanf(" %d", &n);
		memset(pos, 0, sizeof pos);
		foreach (i, n) {
			scanf(" %s", str[i]);
			len[i] = strlen(str[i]);
		}
		merda = false;
		acc= 0;
		for (;pos[0] < len[0];) {
			car = str[0][pos[0]++];
			act = 1;
			med = -1;
			foreach (i, n) {
				while (pos[i] < len[i] && str[i][pos[i]] == car) {
					act++, pos[i]++;
				}
				if (act == 0) {
					merda = true;
				} else {
					att[i] = act;
					if (med == -1)
						med = act;
					else 
						med = (med + act) / 2;
					act = 0;
				}
			}
			foreach (i, n) {
				acc += max(att[i], med) - min(att[i], med);
			}
		}
		foreach (i, n) {
			if (pos[i] < len[i]) {
				merda = true;
				break;
			}
		}
		if (merda) {
			printf("Case #%d: Fegla Won\n", it+1);
		} else {
			printf("Case #%d: %d\n", it+1, acc);
		}
	}
	return 0;
}


