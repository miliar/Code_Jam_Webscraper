#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;
int T;
int main() {
	scanf("%d", &T);
	char str[5000], ans[5000];
	for (int time = 1; time <= T; time++) {
		scanf("%s", str);
		memset(ans, 0, sizeof(ans));
		int head, tail;
		head = tail = 2500;
		printf("Case #%d: ", time);
		for (int i = 0; i < strlen(str); i++) {
			int tmp = head;
			for (tmp = head; str[i] == ans[tmp] && tmp < tail; tmp++) {}
			if (ans[tmp] > str[i]) {
				ans[tail++] = str[i];
			}
			else {
				ans[--head] = str[i];
			}
		}
		for (int i = head; i < tail; i++)
			printf("%c", ans[i]);
		printf("\n");
	}
}