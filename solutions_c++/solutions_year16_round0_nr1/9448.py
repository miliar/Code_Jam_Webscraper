#define _CRT_SECURE_NO_WARNINGS
//자료구조
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional> //greater, less
#include <unordered_map>
#include <unordered_set>

#include <tuple>
#include <utility>

#include <iostream>
#include <string>
#include <cstring>
#include <memory>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD (i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORI(i,a,b) for(int i=(a);i<=(b);++i)
#define FORID(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int casenums = 0;
	scanf("%d", &casenums);
	FORI(casenum, 1, casenums) {
		int num = 0;
		scanf("%d", &num);
		if (num == 0) {
			printf("Case #%d: INSOMNIA\n", casenum);
			continue;
		}
		int multi = 1;
		vector<int> check(10,0);
		int checkcnt = 10;
		int ret = 0;

		while (1) {
			int now = num * multi;
			char dd[100];
			_itoa(now, dd, 10);
			int len = strlen(dd);
			FOR(i, 0, len) {
				char ff = dd[i];
				int kk = atoi(&ff);
				/*cout << kk << "      " << checkcnt << endl;
				cout << check[kk]<<endl;*/
				if (check[kk] == 0) {
					check[kk] = 1;
					checkcnt--;
				}
				if (checkcnt == 0) {
					ret = now;
					goto out;
				}
			}
			multi++;
		}
	out:
		printf("Case #%d: %d\n", casenum,ret);
	}
}
