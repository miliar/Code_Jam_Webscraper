#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <iostream>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

const int MAX = 40;
int n, j;

void clear() {
}

void read() {
	scanf("%d%d", &n, &j);
}

string compose(int t) {
	string s(n, '0');
	s[0] = s[n - 1] = '1';
	string st;
	while (t) {
		int d = t % 2;
		st.push_back(d + '0');
		t /= 2;
	}
	for (int i = 0; i < st.size(); i++)
		s[n - 2 - i] = st[i];
	return s;
}

vi check(string s) {
	vi res;
	for (int b = 2; b <= 10; b++) {
		for (int d = 2; d < 100; d++) {
			int rem = 0;
			for (int i = 0; i < s.size(); i++)
				rem = (rem * b + s[i] - '0') % d;
			if (rem == 0) {
				res.push_back(d);
				break;
			}
		}
	}
	return res;
}

vector<pair<string, vi>> solve() {
	vector<pair<string, vi>> res;
	int t = 0;
	for (int i = 0; i < j; t++) {
		string s = compose(t);
		vi divs = check(s);
		if (divs.size() == 9) {
			res.push_back(make_pair(s, divs));
			i++;
		}
	}
	return res;
}

int main() {
#ifdef _LOCAL_VAN
	freopen("C-large.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		clear();
		read();
		vector<pair<string, vi>> res = solve();
		printf("Case #%d:\n", i);
		for (int i = 0; i < res.size(); i++) {
			printf("%s ", res[i].first.c_str());
			for (int j = 0; j < res[i].second.size(); j++)
				printf(j == res[i].second.size() - 1 ? "%d\n" : "%d ", res[i].second[j]);
		}
	}
	printf("\n");
	return 0;
}