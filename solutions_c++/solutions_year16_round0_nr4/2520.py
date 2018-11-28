#include <iostream>
#include <cstdio>
#include <cstring>  
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;
 
int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n, m, k;
		scanf("%d%d%d", &n, &m, &k);
		printf("Case #%d:", o + 1);
		for (int i = 0; i < n; ++i) {
			printf(" %d", i + 1);
		}
		printf("\n");
	}
	return 0;
}


