using namespace std;
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>


int main()
{
	int i, j, t, n, x, mask;
	ifstream cin("data.in");
	ofstream cout("data.out");

	cin >> t;
	for (i = 1; i <= t; ++i)
	{
		cin >> n;

		if (n == 0)
		{
			cout << "Case #" << i << ": INSOMNIA\n";
		}
		else
		{
			for (mask = 0, j = 1; ; ++j)
			{
				for (x = j * n; x; x /= 10)
					mask |= (1 << (x % 10));

				if (mask == (1 << 10) - 1) break;
			}

			cout << "Case #" << i << ": " << j * n << '\n';
		}
	}

    return 0;
}
