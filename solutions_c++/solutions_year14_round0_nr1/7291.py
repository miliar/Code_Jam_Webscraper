#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
	freopen("A-small-attempt0 (3).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int testCase;
	cin >> testCase;
	int caseNumber = 0;
	while (testCase--) {
		int f[17];
		memset(f, 0, sizeof(f));
		int r1;
		
		cin >> r1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int data;
				cin >> data;
				if (i == r1 - 1) {
					f[data]++;
				}
			} 
		cin >> r1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int data;
				cin >> data;
				if (i == r1 - 1) {
					f[data]++;
				}
			}
		int res = -1, cnt = 0; 
		for (int i = 1; i <= 16; ++i) {
			if (f[i] == 2) {
				res = i;
				++cnt;
			}
		}
		printf("Case #%d: ", ++caseNumber);
		if (res == -1) printf("Volunteer cheated!\n");
		else if (cnt >= 2) printf("Bad magician!\n");
		else printf("%d\n", res);
	}
} 
