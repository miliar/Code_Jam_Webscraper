#include <bits/stdc++.h>
using namespace std;
void init_ios() {ios_base::sync_with_stdio(false); cin.tie(nullptr);}

const char* solve(char* S) {
	string res;
	while (*S) {
		if (!res.size()) res += *S;
		else {
			if (res.front() <= *S) res = *S + res;
			else res += *S;
		}
		++S;
	}
	return res.c_str();
}

int main() {
	int T;
	char S[1001];
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%s", S);
		printf("Case #%d: %s\n", i, solve(S));
	}
	return 0;
}
