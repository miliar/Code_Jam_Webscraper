
#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for(int cse = 1; cse <= T; cse++) {
		int res = 0, clapping = 0, S;
		string str;
		cin >> S >> str;
		for(int i = 0; i < str.length(); i++) {
			int num = str[i] - '0';
			if(!num) continue;
			if(clapping < i)
				res += i-clapping,
				clapping += i-clapping;
			clapping += num;
		}

		printf("Case #%d: %d\n", cse, res);
	}
	return 0;
}
