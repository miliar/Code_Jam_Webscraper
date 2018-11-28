
#include<bits/stdc++.h>
#include <pthread.h>

using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tc;
	scanf("%d", &tc);
	for (int kk = 1; kk <= tc; kk++) {
		string str;
		cin >> str;
		str.erase(std::unique(str.begin(), str.end()), str.end());
		int ans;
		if (str[str.length() - 1] == '+')
			ans = str.length() - 1;
		else
			ans = str.length();

		printf("Case %d: %d\n", kk, ans);
	}


	return 0;
}

















