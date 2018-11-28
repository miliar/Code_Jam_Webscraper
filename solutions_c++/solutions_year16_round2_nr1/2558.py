#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

int num[16], freq[32];
char buf[2016];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;
		
		scanf("%s", buf);
		int n = strlen(buf);
		memset(freq, 0, sizeof(freq));
		for (int i = 0; i < n; ++i) {
			freq[buf[i] - 'A']++;
		}
		num[0] = freq['Z' - 'A'];
		freq['Z' - 'A'] -= num[0];
		freq['E' - 'A'] -= num[0];
		freq['R' - 'A'] -= num[0];
		freq['O' - 'A'] -= num[0];

		num[2] = freq['W' - 'A'];
		freq['T' - 'A'] -= num[2];
		freq['W' - 'A'] -= num[2];
		freq['O' - 'A'] -= num[2];

		num[4] = freq['U' - 'A'];
			freq['F' - 'A'] -= num[4];
			freq['O' - 'A'] -= num[4];
			freq['U' - 'A'] -= num[4];
			freq['R' - 'A'] -= num[4];

		num[1] = freq['O' - 'A'];
			freq['O' - 'A'] -= num[1];
			freq['N' - 'A'] -= num[1];
			freq['E' - 'A'] -= num[1];
		
		num[3] = freq['R' - 'A'];
			freq['T' - 'A'] -= num[3];
			freq['H' - 'A'] -= num[3];
			freq['R' - 'A'] -= num[3];
			freq['E' - 'A'] -= num[3] * 2;
		
		num[5] = freq['F' - 'A'];
			freq['F' - 'A'] -= num[5];
			freq['I' - 'A'] -= num[5];
			freq['V' - 'A'] -= num[5];
			freq['E' - 'A'] -= num[5];
		
		num[6] = freq['X' - 'A'];
		freq['S' - 'A'] -= num[6];
		freq['I' - 'A'] -= num[6];
		freq['X' - 'A'] -= num[6];
		
		num[7] = freq['S' - 'A'];
		freq['S' - 'A'] -= num[7];
		freq['E' - 'A'] -= num[7] * 2;
		freq['V' - 'A'] -= num[7];
		freq['N' - 'A'] -= num[7];

		num[8] = freq['G' - 'A'];
		freq['E' - 'A'] -= num[8];
		freq['I' - 'A'] -= num[8];
		freq['G' - 'A'] -= num[8];
		freq['H' - 'A'] -= num[8];
		freq['T' - 'A'] -= num[8];

		num[9] = freq['I' - 'A'];

		for (int i = 0; i <= 9; ++i) {
			for (int j = 0; j < num[i]; ++j) {
				printf("%d", i);
			}
		}
		puts("");
	}
 	return 0;
}