#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
#include <cstring>
using namespace std;

map<string, int> visit;

string rev(string S, int x) {
	string ret = S;
	for (int i = 0; i <= x; i++) {
		if (S[x - i] == '+')
			ret[i] = '-';
		else
			ret[i] = '+';
	}
	return ret;
}

string rev(string S) {
	string ret = S;
	for (int i = 0; i < S.size(); i++)
		ret[i] = S[i] == '+' ? '-' : '+';
	return ret;
}

int go(string S) {
	int n = S.length();
	int ret = 2 * n;

	if (n == 0)
		return 0;
	if (S[n - 1] == '+')
		return go(S.substr(0, n - 1));
	if (visit.count(S))
		return visit[S];
	visit[S] = -1;

	int count1 = go(rev(S.substr(0, n - 1)));
	if (count1 != -1)
		ret = min(ret, count1 + 1);
	int count2 = go(rev(S, n - 1));
	if (count2 != -1)
		ret = min(ret, count2 + 1);
	visit[S] = ret;
	return ret;
}

int main(void) {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		char S[101];
		scanf("%s", S);
		visit.clear();
		printf("Case #%d: %d\n", tc, go(string(S)));
	}
	return 0;
}
