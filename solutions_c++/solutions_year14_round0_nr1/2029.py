#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <math.h>
#include <cstdio>
using namespace std;

int main() {
	int T = 0;
	scanf("%d", &T);
	int k = 0;
	while(k < T) {
		vector< vector< vector<int> > > ans;
		ans.resize(4);
		for(int i = 0; i < 4; i++) {
			ans[i].resize(4);
		}
		int a1 = -1, a2 = -1;
		int temp = 0;
		scanf("%d", &a1);
		a1 -= 1;
		map<int, pair<int, int> > dict;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				scanf("%d", &temp);
				pair<int, int> np (i, -1);
				dict[temp] = np;
			}
		}
		scanf("%d", &a2);
		a2 -= 1;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				scanf("%d", &temp);
				dict[temp].second = i;
			}
		}
		for(int i = 1; i <= 16; i++) {
			int w1 = dict[i].first;
			int w2 = dict[i].second;
			ans[w1][w2].push_back(i);
		}
		if(ans[a1][a2].size() == 1) {
			printf("Case #%d: %d\n", k+1, ans[a1][a2][0]);
		}
		else if(ans[a1][a2].size() == 0) {
			printf("Case #%d: Volunteer cheated!\n", k+1);
		}
		else {
			printf("Case #%d: Bad magician!\n", k+1);
		}
		k++;
	}
	return 0;
}