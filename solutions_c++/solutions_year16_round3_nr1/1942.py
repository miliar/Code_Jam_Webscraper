#include <stdio.h>
#include <algorithm>
#include <set>
#include <functional>
#pragma warning(disable:4996)
using namespace std;
int P[33];
set<pair<int, char>> cho;
int main(){
	int tcase;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &tcase);
	for (int i1 = 1; i1 <= tcase; i1++){
		cho.clear();
		printf("Case #%d:", i1);
		int n,hap = 0; scanf("%d", &n);
		for (int i = 1; i <= n; i++){
			scanf("%d", &P[i]);
			cho.insert(make_pair(P[i], i + 'A' - 1));
			hap = hap + P[i];
		}
		int maj = 0;
		while (hap > 0){
			printf(" ");
			// 1
			set<pair<int, char>>::iterator p;
			p = cho.end();
			pair<int, char> tmp = *(--p);
			cho.erase(tmp); printf("%c", tmp.second);
			tmp.first = tmp.first - 1;
			cho.insert(tmp); hap--;
			// 2
			bool flag = true;
			maj = (hap-1) / 2;
			p = cho.end();
			tmp = *(--p);
			cho.erase(tmp);
			for (p = cho.begin(); p != cho.end(); ++p){
				if (p->first > maj){
					flag = false;
					break;
				}
			}
			if (flag && tmp.first-1 <= maj){
				printf("%c", tmp.second);
				tmp.first = tmp.first - 1;
				hap--;
			}
			cho.insert(tmp);
		}
		printf("\n");
	}
	return 0;
}