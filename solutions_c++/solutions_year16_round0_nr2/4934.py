#pragma comment(linker, "/STACK:134217728")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <complex>
#include <functional>
#include <cmath>
#include <time.h>

using namespace std;

typedef long long LL;


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	int numberTest = 1;
	while (t--) {
		string s;
		cin >> s;
		int cnt = 0;
		if (s[0] == '-') {
			cnt--;
		}
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				while (i < s.size() && s[i] == '-') {
					i++;
				}
				cnt += 2;
			}
		}
		printf("Case #%d: %d\n", numberTest++, cnt);
	}
	return 0;
}