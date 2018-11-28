#include <iostream>
#include <fstream>

using namespace std;

int T, sz;
char S;

int main()
{
	ifstream in ("A.in");
	ofstream out ("A.out");

	long long sum, ans;
	int i, j;

	in >> T;

	j = 1;
	while (j <= T)
	{
		in >> sz;

		sum = 0;
		ans = 0;

		i = 0;
		while (i <= sz)
		{
			in >> S;

			if (sum < i)
			{
				ans += i - sum;
				sum = i;
			}

			sum += int (S) - 48;
			i++;
		}

		out << "Case #" << j << ": " << ans << endl;
		j++;
	}

	in.close();
	out.close();

	return 0;
}