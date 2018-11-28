#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int findMax(int * n, int x)
{
	int max = n[0];

	for (int i = 1; i < x; i++)
	{
		if (max < n[i])
		{
			max = n[i];
		}
	}

	return max;
}

int main()
{
	ofstream out("code.txt");
	ifstream in("B-large.in");
	int k, *n, x;
	string num, name;
	bool ch = true;
	in >> k;

	for (int j1 = 0; j1 < k; j1++)
	{
		in >> x;

		n = new int[x];

		for (int i = 0; i < x; i++)
		{
			in >> n[i];
		}

		int min1, max1, sum;


		max1 = findMax(n, x);

		min1 = max1;
		for (int i = 1; i <= max1; i++) {
			sum = i;
			for (int j = 0; j < x; j++) {
				if (n[j] > i) {
					if (n[j] % i == 0)
						sum += (n[j] / i - 1);
					else
						sum += (n[j] / i);
				}
			}

			if (min1 > sum)
				min1 = sum;
		}		

		out << "Case #" << j1 + 1 << ": " << min1 << endl;
	}


	return 0;
}
