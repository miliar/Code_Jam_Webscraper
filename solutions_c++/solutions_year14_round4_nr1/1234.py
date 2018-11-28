#include <iostream>
#include <fstream>

using namespace std;



int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t; fin >> t;
	for (int test = 0; test < t; test++)
	{
		int n, x;
		fin >> n >> x;

		int weights[n];
		bool hit[n];

		for (int i = 0; i < n; i++)
		{
			fin >> weights[i];
			hit[i] = false;
		}

		sort(weights, weights + n);
		int ans = 0;

		for (int bigp = n - 1; bigp >= 0; bigp--)
		{
			if (!hit[bigp])
			{
				bool flag = false;
				for (int lilp = bigp - 1; lilp >= 0; lilp--)
				{
					
					if (!flag && !hit[lilp] && weights[bigp] + weights[lilp] <= x)
					{
						hit[bigp] = hit[lilp] = true;
						ans++;
						flag = true;
					}
				}
				if (!flag)
				{
					hit[bigp] = true;
					ans++;
				}
			}
		}
		cout << test << endl;
		fout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}