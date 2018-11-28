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

int main () {
	int n, t, a, b, k, acc;
	scanf(" %d", &t);
	foreach (it, t) {
		scanf(" %d %d %d", &a, &b, &k);
		acc = 0;
		foreach (i, a) {
			foreach (j, b) {
				if ((i & j) < k) {
					acc++;
				}
			}
		}
		printf("Case #%d: %d\n", it+1, acc);
	}
	return 0;
}


