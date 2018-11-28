#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in ("B-large.in");
	ofstream out ("B-large.out");

	int T, t, temp;

	in >> T;

	t = 1;
	while (t <= T)
	{
		int N, i, j, A[2501] = {0};

		out << "Case #" << t << ": ";

		in >> N;

		i = 0;
		while (i < 2 * N - 1)
		{
			j = 0;
			while (j < N)
			{
				in >> temp;

				A[temp]++;

				j++;
			}

			i++;
		}

		i = 1;
		while (i < 2501)
		{
			if (A[i] % 2)
				out << i << " ";

			i++;
		}

		out << endl;

		t++;
	}

	in.close();
	out.close();

	return 0;
}