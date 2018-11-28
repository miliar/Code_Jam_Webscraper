#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-input.txt", "r", stdin);
	freopen("A-output.txt", "w", stdout);
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int R, C, W, result, temp;
		cin >> R >> C >> W;

		result = (C / W * R) + (W - 1);
		if (C % W > 0) result++;

		cout << "Case #" << t << ": " << result << "\n";
	}

	return 0;
}
