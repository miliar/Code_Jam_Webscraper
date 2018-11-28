#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

ifstream in("c2.in");
ofstream out("c2.out");

int main()
{
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		int answer = 0, c, d, v;
		in >> c >> d >> v;
		vector <int> f;
		for (int i = 0; i < d; ++i)
		{
			int k;
			in >> k;
			for (int j = 0; j < c; ++j)
				f.push_back(k);
		}
		bool zibil = true;
		while (zibil)
		{
			zibil = true;
			sort(f.begin(), f.end());
			if (f[0] != 1)
			{
				for (int j = 0; j < c; ++j)
					f.push_back(1);
				answer++;
				continue;
			}
			int sum = 0;
			for (int i = 0; i < f.size(); ++i)
			{
				sum += f[i];
				if (sum >= v)
				{
					zibil = false;
					break;
				}
				if (i == f.size() - 1 || f[i + 1] > sum + 1)
				{
					for (int j = 0; j < c; ++j)
						f.push_back(sum + 1);
					//cout << sum + 1 << endl;
					answer++;
					break;
				}
			}
		}
		out << "Case #" << t << ": " << answer << endl;
	}
}