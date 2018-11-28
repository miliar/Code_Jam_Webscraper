/*
 * a.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: mamdouh
 */




#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

#define pb push_back
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("ans.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		int r1,r2;
		scanf("%d", &r1);
		vector<int  >v1,v2;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int cur;
				scanf("%d", &cur);
				if(i+1==r1)
					v1.pb(cur);
			}
		}
		scanf("%d", &r2);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int cur;
				scanf("%d", &cur);
				if(i+1==r2)
					v2.pb(cur);
			}
		}
		vector<int > match;
		for (int i = 0; i < v1.size(); ++i) {
			for (int j = 0; j < v2.size(); ++j) {
				if(v1[i] == v2[j])
					match.pb(v1[i]);
			}
		}
		printf("Case #%d: ", ii+1);
		if(match.size()==0)
			printf("Volunteer cheated!");
		else if(match.size()==1)
			printf("%d", match.back());
		else printf("Bad magician!");
		printf("\n");
	}

	return 0;
}
