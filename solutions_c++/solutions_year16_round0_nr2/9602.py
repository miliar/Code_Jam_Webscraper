#include <vector>
#include <stdio.h>
#include <iostream>
#include <map>
#include <cassert>
#include <cmath>
#define pb push_back
#define mp make_pair
#define F first
#define S second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
const int N = (int)105;


int n;
char s[10000];

int main () {
	freopen("in0.in", "r", stdin);
	freopen("out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%s", s);
		int n = strlen(s);
		vector<pii> v;
		for (int i = 0; i < n; i++) {
			if (!v.empty() && s[i] == v.back().F)
				v.back().S++;
			else
				v.pb(mp(s[i], 1));
		}
		if (v.back().F == '+')
			v.pop_back();
		printf("%d\n", (int)v.size());
	}
	return 0;
}


