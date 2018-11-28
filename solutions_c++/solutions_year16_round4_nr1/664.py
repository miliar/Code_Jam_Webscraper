#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <set>
#include <map>
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
// head
struct Node {
	string str;
	int r, p, s;
	Node(string str, int r, int p, int s) : str(str), r(r), p(p), s(s) {}
	Node() {}

	Node add(Node &o) {
		Node temp;
		temp.str = min(str + o.str, o.str + str);
		temp.r = r + o.r;
		temp.p = p + o.p;
		temp.s = s + o.s;
		return temp;
	}
};

Node a[15][3];

void init() {
	a[1][0] = Node("PS", 0, 1, 1);// S
	a[1][1] = Node("RS", 1, 0, 1);// R
	a[1][2] = Node("PR", 1, 1, 0);// P
	for (int i = 2; i <= 12; i++) {
		a[i][0] = a[i-1][0].add(a[i-1][2]);
		a[i][1] = a[i-1][1].add(a[i-1][0]);
		a[i][2] = a[i-1][2].add(a[i-1][1]);
	}
}

int main() {
	freopen("out1.txt", "w", stdout);
	init();
	int t, n, r, p, s, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d%d", &n, &r, &p, &s);
		bool flag = false;
		printf("Case #%d: ", cas++);
		for (int i = 0; i < 3; i++) {
			if (a[n][i].p == p && a[n][i].s == s && a[n][i].r == r) {
				flag = true;
				printf("%s\n", a[n][i].str.c_str());
				break;
			}
		}
		if (!flag) puts("IMPOSSIBLE");
	}
	return 0;
}
