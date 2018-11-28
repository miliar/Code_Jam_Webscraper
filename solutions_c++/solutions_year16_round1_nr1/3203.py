
#define _CRT_SECURE_NO_WARNINGS
//자료구조
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional> //greater, less

#include<tuple>
#include <utility>

#include <iostream>
#include <string>
#include <cstring>
#include <memory>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(a);i>(b);--i)
#define FORI(i,a,b) for(int i=(a);i<=(b);++i)
#define FORID(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

int main() {
	freopen("in.txt", "r", stdin);
	freopen("C:\\Users\\seok\\Desktop\\out.txt", "w", stdout);
	int casenums = 0;
	scanf("%d", &casenums);
	for (int casenum = 1; casenum <= casenums; ++casenum) {
		char input[1001];
		scanf("%s", input);
		int len = strlen(input);

		string ret;
		FOR(i, 0, len) {
			char now = input[i];
			if (now >= ret[0]) {
				ret = now + ret;
			}
			else {
				ret = ret + now;
			}
		}

		//입출력
		printf("Case #%d: ", casenum);
		cout << ret << endl;
	}
}
