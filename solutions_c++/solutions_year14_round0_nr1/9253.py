#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;



int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		pair<int, int> tab[16];
		for (int i=0; i<16; i++) tab[i]=make_pair(0, i);
		for (int k=0; k<2; k++) {
			int x;
			scanf("%d", &x);
			x--;
			for (int i=0; i<4; i++) {
				for (int j=0; j<4; j++) {
					int a;
					scanf("%d", &a);
					a--;
					if (i==x) tab[a].first++;
				}
			}
		}
		sort(tab, tab+16);
		if (tab[15].first<2) printf("Volunteer cheated!");
		else if (tab[14].first==2) printf("Bad magician!");
		else printf("%d", tab[15].second+1);
		printf("\n");
	}
	return 0;
}
