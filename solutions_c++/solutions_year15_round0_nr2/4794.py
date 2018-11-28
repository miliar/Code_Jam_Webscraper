#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int a[2000];
	int b[2000];
	ifstream input("B-small-attempt4.in");
	ofstream output("output.txt");
	int num;
	int m;
	input >> num;
	for (int n = 0; n < num; n++)
	{
		output << "Case #" << n + 1 << ": ";
		input >> m;
		for (int i = 0; i < m; i++)
		{
			input >> a[i];
			b[i] = a[i];
		}
		sort(a, a + m);
		sort(b, b + m);
		int max = a[m - 1];
		int min = max;
		int i = 1;
		if (a[m - 1] == 9)
		{
			int j = 0;
			int m1 = m;
			while (j < max)
			{
				if (b[m1 - 1] == 9)
				{
					j += 2;
					b[m1 - 1] = 3;
					b[m1] = 3;
					b[m1 + 1] = 3;
					m1 += 2;
					sort(b, b + m1);
					if (b[m1 - 1] + j < min)
						min = b[m1 - 1] + j;
				}
				else
				{
					j++;
					int a1 = b[m1 - 1] / 2;
					int a2 = b[m1 - 1] - a1;
					b[m1 - 1] = a1;
					b[m1] = a2;
					m1++;

					sort(b, b + m1);
					if (b[m1 - 1] + j < min)
						min = b[m1 - 1] + j;
				}
			}
		}
		while (i < max)
		{
			int a1 = a[m - 1] / 2;
			int a2 = a[m - 1] -  a1;
			a[m - 1] = a1;
			a[m] = a2;
			m++;
			sort(a, a + m);
			if (a[m - 1] + i < min)
				min = a[m - 1] + i;
			i++;
		}
		output << min << endl;
	}
}