#include <fstream>
#include <vector>

int main()
{
	std::ifstream in("test.txt");
	std::ofstream out("out.txt");

	int T = 0;

	in >> T;

	for (int i = 0; i < T; i++)
	{
		long long a, b;

		in >> a >> b;

		long long count = 0, j = 0;

		while (j * j < a)
			j++;

		while (j * j <= b)
		{
			long long t = j * j, n = 0, r = j, m = 0;

			while (t)
			{
				n = n * 10 + t % 10;
				t /= 10;
			}

			while (r)
			{
				m = m * 10 + r % 10;
				r /= 10;
			}

			if ((j * j == n) && (j == m))
				count++;
			j++;
		}

		out << "Case #" << i + 1 << ": " << count << std::endl;
	}
}