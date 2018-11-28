#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

const int L = 1e4 + 10;

char st[L];

int get[5][5] = {{},
	{0, 1, 2, 3, 4}, 
	{0, 2, -1, 4, -3}, 
	{0, 3, -4, -1, 2}, 
	{0, 4, 3, -2, -1}};

int change(char a) {
	if (a == 'i') return 2;
	if (a == 'j') return 3;
	return 4;
}

int main() {
	//freopen("c.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for (int s = 1; s <= TT; s++) {
		int l, x;
		scanf("%d%d", &l, &x);
		scanf("%s", st);
		bool flag = 0, one = 0, two = 0;
		int now = 1;
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < l; j++) {
				now = get[now][change(st[j])];
				if (now < 0) {
					flag = !flag;
					now = -now;
				}
				if (!one) {
					if (!flag && now == 2) one = 1;
				}
				else if (!two) {
					if (!flag && now == 4) two = 1;
				}
			}
		}
		printf("Case #%d: ", s);
		if (one && two && now == 1 && flag) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}

