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

	string s;
	cin >> s;
	int cnt = 0;
	for (int i = 1; i < (int)s.length(); i++){
		if (s[i] != s[i - 1])
			cnt++;
	}
	if (s.back() == '-')
		cnt++;

	printf("%d\n", cnt);
}

int main(){

	int T = nxt();
	for (int i = 0; i < T; i++){
		solve(i + 1);
		cerr << "Test #" << i + 1 << " is complete\n";
	}

	return 0;
}