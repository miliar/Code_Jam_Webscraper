#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

void solve(int test){
	printf("Case #%d: ", test);

	int n = nxt();
	if (n == 0){
		printf("INSOMNIA\n");
		return;
	}

	int cnt = 0;
	vector<char> dg(10);
	while (1){
		cnt++;
		long long m = 1ll * cnt * n;
		while (m){
			dg[m % 10] = 1;
			m /= 10;
		}
		char ok = 1;
		for (int i = 0; i < 10; i++)
			ok &= dg[i];
		if (ok)
			break;
	}
	printf("%lld\n", 1ll * n * cnt);
}

int main(){

	int T = nxt();
	for (int i = 0; i < T; i++){
		solve(i + 1);
		cerr << "Test #" << i + 1 << " is complete\n";
	}

	return 0;
}