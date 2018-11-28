#include <bits/stdc++.h>

using namespace std;

int T, N, J;
string s;

long long cal(long long x) {
	long long res = 0;
	long long p = 1;
	int n = s.size();
	for(int i = n - 1; i >= 0; i--) {
		res += (s[i] - '0') * p;
		p *= x;
	}
	return res;
}

void add() {
	int jin = 2;
	int n = s.size();
	for(int i = n - 1; i >= 0; i--) {
		int a = s[i] - '0' + jin;
		if(a > 1) jin = 1, a -= 2;
		else jin = 0;
		s[i] = char(a + '0');
		if(jin == 0) break;
	}
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("ans1.txt","w",stdout);

	scanf("%d", &T);
	int cas = 0;
	while(T--) {
		printf("Case #%d:\n", ++cas);
		scanf("%d%d", &N, &J);
		if(N == 16) s = "10000001";
		else s = "1000000000000001";
		for(int i = 1; i <= J; i++) {
			printf("%s%s", s.c_str(), s.c_str());
			for(int k = 2; k <= 10; k++) {
				printf(" %lld", cal(k));
			}
			printf("\n");
			add();
		}
	}
}