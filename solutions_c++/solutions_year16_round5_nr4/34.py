#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int t;
int n, l;
set <string> allowed;
string tmp;

char Inv(char ch) { return ch == '0'? '1': '0'; }

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &n, &l);
		allowed.clear();
		while (n--) {
			cin >> tmp;
			allowed.insert(tmp);
		}
		cin >> tmp;
		printf("Case #%d: ", tc);
		if (allowed.find(tmp) != allowed.end()) printf("IMPOSSIBLE\n");
		else {
			for (int i = 0; i < l - 1; i++)
				printf("%c%c", Inv(tmp[i]), tmp[i]);
			printf("%c ", Inv(tmp[l - 1]));
			for (int i = 0; i < l; i++)
				printf("%c?", Inv(tmp[i]));
			printf("\n");
		}
	}
	return 0;
}