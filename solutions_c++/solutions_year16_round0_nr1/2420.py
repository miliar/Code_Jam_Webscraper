#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");

	int T, N, i, j, a[10], count;
	long long int ans, temp;

	in >> T;

	i = 1;
	while (i <= T)
	{
		out << "Case #" << i << ": ";

		in >> N;

		if (N)
		{
			j = 0;
			while (j < 10)
			{
				a[j] = 0;

				j++;
			}

			count = 10;
			ans = 0;
			while (count)
			{
				ans += N;

				temp = ans;
				while (temp)
				{
					if (!a[temp % 10])
						count--;

					a[temp % 10]++;

					temp /= 10;
				}
			}
			
			out << ans;
		}
		else
			out << "INSOMNIA";

		out << endl;

		i++;
	}

	in.close();
	out.close();

	return 0;
}