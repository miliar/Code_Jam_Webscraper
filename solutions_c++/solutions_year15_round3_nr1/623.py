#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <queue>
#include <map>
#include <set>
 

using namespace std;


int t;
int r, w, c;


int main(){
	freopen("input.txt", "r", stdin);
	freopen("codi1.out", "w", stdout);
	cin >> t;
	for (int j = 0; j < t; j++) {
		cin >> r >> c >> w;
		printf("Case #%d: %d\n", j + 1, (r - 1) * (c / w) + c / w - 1 + w + (c % w != 0 ? 1: 0));
	}
 	return 0;
}
