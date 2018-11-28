#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	//http://www.cplusplus.com/reference/cstdio/freopen/
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int tc;
	//http://www.cplusplus.com/reference/cstdio/scanf/
	scanf("%d", &tc);
	for (int i=1; i <= tc; i++) {
		printf("Case #%d: ", i);
		int Smax, invite = 0;
		char audience[1001];
		scanf("%d", &Smax);
		scanf("%s", audience);
		//http://www.cplusplus.com/forum/beginner/68260/
		int standing = (int) audience[0] - '0';
		for (int j = 1; j <= Smax; j++) {
			int ppl = (int) audience[j] - '0';
			if (j > standing && ppl > 0) {
				invite += j - standing;
				standing += ppl + invite;
			} else {
				standing += ppl;
			}
		}
		//printf("%d, %d, %s\n", invite, Smax, audience);
		printf("%d\n", invite);
	}
	return 0;
}
