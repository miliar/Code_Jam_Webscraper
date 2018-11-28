/*
 * MagicTrick.cpp
 * run command
 * g++ /media/program/cprogram/git_repo/Algorithm/src/codejam/2014/MagicTrick.cpp -o /usr/build/Main.o
 *
 *  Created on: Apr 12, 2014
 *      Author: Indresh Gahoi
 */

#include<iostream>
#include<sstream>
#include<fstream>
#include<cstdio>
#include<climits>
#include<pthread.h>
#include<sys/types.h>
#include<unistd.h>
#include<algorithm>
#include<string>
#include<cstring>
#include<set>
#include<vector>
#include<map>
#include<stack>
#include<queue>

using namespace std;

int main() {

	int x;
	int hash[17];
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","rw",stdout);
	int T;
	scanf("%d", &T);
	int ans1, ans2, key;
	for (int t = 1; t <= T; ++t) {
		memset(hash, 0, sizeof(hash));
		scanf("%d", &ans1);
		ans1--;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &x);
				if (i == ans1) {
					hash[x] = 1;
				}
			}
		}

		scanf("%d", &ans2);
		ans2--;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &x);
				if (i == ans2) {
					if (hash[x] == 1) {
						key = x;
						hash[0]++;
					}
				}
			}
		}
		if (hash[0] == 0) {
			printf("Case #%d: %s\n", t, "Volunteer cheated!");	// case hash[0] > 1
		} else if (hash[0] == 1) {
			printf("Case #%d: %d\n", t, key);
		} else {
			printf("Case #%d: %s\n", t, "Bad magician!");
		}
	}

}

