#include <fstream>

using namespace std;

int main()
{
	int T;
	int n, p[999];

	ifstream in("input.txt");
	ofstream out("output.txt");

	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		in >> n;

		int sum = 0;
		for (int i = 0; i < n; ++i)
		{
			in >> p[i];
			sum += p[i];
		}

		out << "Case #" << t << ": ";

		while (0 < sum)
		{
			int max1 = 0, max2 = 0;
			int max1_index = -1, max2_index = -1;

			for (int i = 0; i < n; ++i)
			{
				if (max1 < p[i])
				{
					max1 = p[i];
					max1_index = i;
				}
			}

			p[max1_index]--;
			sum--;

			for (int i = 0; i < n; ++i)
			{
				if (max2 < p[i])
				{
					max2 = p[i];
					max2_index = i;
				}
			}

			if (max2 == 0)
			{
				out << (char) (max1_index + 'A') << " ";
			}
			else
			{
				p[max2_index]--;
				sum--;

				bool flag = true;
				for (int i = 0; i < n; ++i)
				{
					if (p[i] > sum / 2)
					{
						flag = false;
						break;
					}
				}

				if (flag)
					out << (char)(max1_index + 'A') << (char)(max2_index + 'A') << " ";
				else
				{
					p[max2_index]++;
					sum++;
					out << (char)(max1_index + 'A') << " ";
				}
			}
		}

		out << endl;
	}

	return 0;
}