#include <iostream>

void solve()
{
	int R, C, W;
	std::cin >> R >> C >> W;

	int y = C/W + W;
	if (C%W == 0)
	{
		y--;
	}

	std::cout << y;

}

int main()
{
	int T;
	std::cin >> T;
	for (int X = 1; X <= T; X++)
	{
		std::cout << "Case #" << X << ": ";
		solve();
		std::cout << "\n";
	}
}