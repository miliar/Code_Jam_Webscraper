#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	char str[2010];
	int count[30];
	for (int t = 0; t < T; t++) {
		scanf("%s", str);
		memset(count, 0, sizeof(count));
		for (int i = 0; i < strlen(str); i++) {
			count[str[i] - 'A']++;
		}
		int a[20];
		a[0] = count['Z' - 'A'];
		a[2] = count['W' - 'A'];
		a[8] = count['G' - 'A'];
		a[3] = count['T' - 'A'] - a[2] - a[8];
		a[4] = count['R' - 'A'] - a[0] - a[3];
		a[5] = count['F' - 'A'] - a[4];
		a[7] = count['V' - 'A'] - a[5];
		a[6] = count['S' - 'A'] - a[7];
		a[9] = count['I' - 'A'] - a[5] - a[6] - a[8];
		a[1] = count['O' - 'A'] - a[0] - a[2] - a[4];
		printf("Case #%d: ", t + 1);
		for (int i = 0; i <= 9; i++) {
			for (int j = 0; j < a[i]; j++)
				printf("%d", i);
		}
		printf("\n");
	}
}
