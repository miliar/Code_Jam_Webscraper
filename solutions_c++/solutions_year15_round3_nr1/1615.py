#include <iostream>

using namespace std;

int main()
{
	int T; cin >> T;

	for (int t = 0; t < T; t++)
	{
		int R, C, W;
		cin >> R >> C >> W;

		int result = C / W - 1;

		int to_be_checked = C % W + W;
		
		if (to_be_checked == W)
		{
			result += W;
		}
		else
		{
			result += (W + 1);
		}

		cout << "Case #" << t + 1 << ": " << result << '\n';
	}

	return 0;
}