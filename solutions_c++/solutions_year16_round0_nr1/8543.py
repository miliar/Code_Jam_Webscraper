#include <iostream>

using namespace std;
using uint128 = unsigned __int128;

ostream& operator<<(ostream& stream, const uint128& p_x)
{
	uint128 x = p_x;
	if (x == 0) return stream << '0';

	char buffer[128];
	int top = 0;

	while (x)
	{
		buffer[top++] = x % 10 + '0';
		x /= 10;
	}

	while (top)
		stream.put(buffer[--top]);

	return stream;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		const int dest = 0b1111111111;
		int is = 0;
		int N;
		cin >> N;
		if (N == 0)
		{
			cout << "Case #" << t << ": INSOMNIA\n";
			continue;
		}
		
		uint128 x = 0;
		while (is ^ dest)
		{
			x += N;
			uint128 t = x;
			while (t)
			{
				is |= 1 << (t % 10);
				t /= 10;
			}
		}

		cout << "Case #" << t << ": " << x << '\n';
	}
	return 0;
}
