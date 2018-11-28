#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <functional>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

string m[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int ord[] = { 0, 2, 8, 6, 3, 7, 4, 5, 1, 9 };
char ord2[] = { 'Z', 'W', 'G', 'X', 'T', 'S', 'R', 'F', 'O', 'I' };

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, kase = 0;
	scanf("%d", &T);
	while (++kase <= T) {
		printf("Case #%d: ", kase);
		string s;
		cin >> s;
		int cnt[30] = {};
		int res[10] = {};
		for (char c : s) 
			cnt[c - 'A']++;
		for (int i = 0; i < 10; i++) {
			int n = cnt[ord2[i] - 'A'];
			res[ord[i]] = n;
			for (char c : m[ord[i]]) {
				cnt[c - 'A'] -= n;
			}
		}
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < res[i]; j++)
				printf("%d", i);
		}
		printf("\n");
	}
	return 0;
}