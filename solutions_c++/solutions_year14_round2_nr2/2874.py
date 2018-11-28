#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	freopen("ProblemB.in", "r", stdin);
	freopen("ProblemB.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		unsigned long long a, b, k;
		cin >> a >> b >> k;
		unsigned long long result = 0;
		for (int i = 0; i < a; i++) for (int j = 0; j < b; j++) if ((i & j) < k) result++;
		cout << "Case #" << test + 1 << ": " << result << "\n";
	}

	cout.flush();
	fclose(stdin);
	fclose(stdout);
	return 0;
}
