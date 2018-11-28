#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <cstring>
#include <math.h>
#include<cstdio>
#include<deque>
#include<sstream>
using namespace std;
#define mp make_pair
#define eps 1e-6
int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "w", stdout);

	int t, tt = 1;
	string s;
	scanf("%d", &t);
	while (t--) {
		cin >> s;

		int f = 1, a = 0, b = s.length() - 1;
		int res = 0;
		for (int i = s.length() - 1; i >= 0; i--) {
			if (f && s[b] == '+')
				b--;
			else if (!f && s[a] == '+')
				a++;
			else if (f && s[b] == '-') {
				if (s[a] == '-') {
					res++;
					for (int j = a; j <= b; j++)
						if (s[j] == '+')
							s[j] = '-';
						else
							s[j] = '+';
					a++;
				} else {
					for (int j = a; j < b; j++) {
						if (s[j] == '+')
							s[j] = '-';
						else
							break;
					}
					res += 2;
					for (int j = a; j <= b; j++)
						if (s[j] == '+')
							s[j] = '-';
						else
							s[j] = '+';
					a++;
				}
				f = !f;
			} else if (!f && s[a] == '-') {

				if (s[b] == '-') {
					res++;
					for (int j = a; j <= b; j++)
						if (s[j] == '+')
							s[j] = '-';
						else
							s[j] = '+';
					b--;
				} else {
					for (int j = b; j > a; j--) {
						if (s[j] == '+')
							s[j] = '-';
						else
							break;
					}
					res += 2;
					for (int j = a; j <= b; j++)
						if (s[j] == '+')
							s[j] = '-';
						else
							s[j] = '+';
					b--;
				}
				f = !f;
			}
		}
		printf("Case #%d: %d\n", tt++, res);

	}

	return 0;
}
