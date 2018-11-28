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
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int casenums = 0;
	scanf("%d", &casenums);
	FORI(casenum, 1, casenums) {
		char input[101];
		scanf("%s", input);
		string dd(input);
		int ret = 0;
		int len = dd.length();

		{
			queue<pair<string, int>> que;

			int cnt = 0;
			que.push(make_pair(dd, 0));

			while (!que.empty()) {
				pair<string, int> now = que.front(); que.pop();
				//printf("%s  %d\n", now.first.c_str(), now.second);
				//검사
				int chk = 0;
				char bigyo = now.first[0];
				char opp = bigyo == '+' ? '-' : '+';

				string imsi = string(now.first);
				FOR(i, 0, len) {
					chk = i;
					if (now.first[i] == bigyo) {
						imsi[i] = opp;
					}
					else {
						break;
					}
				}
				//cout << chk << "       " << opp << endl;
				int chk2 = 0;
				FOR(i, 0, len) {
					if (now.first[i] == '-') {
						chk2 = 1;
						break;
					}
				}
				if (chk2 == 0) {
					ret = now.second;
					break;
				}
				else {
					que.push(make_pair(imsi, now.second + 1));
				}
				//if (chk == len - 1 && opp == '+') {//끝까지 그리고 +로
				//	ret = now.second + 1;
				//	break;
				//}
				//else {
				//	que.push(make_pair(imsi, now.second + 1));
				//}

				////bfs
				//FOR(i, 0, len) {//0부터 i까지
				//	string imsi = string(now.first);
				//	FOR(j, 0, i + 1) {
				//		imsi[j] = (now.first[i - j] == '-') ? '+' : '-';
				//	}
				//	que.push(make_pair(imsi, now.second + 1));
				//}
			}
		}

		printf("Case #%d: %d\n", casenum, ret);
	}
}
