#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream in("B2.in");
ofstream out("B2.out");

int main()
{
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n;
		in >> n;
		vector <int> a(n);
		for (int i = 0; i < n; ++i)
			in >> a[i];
		int answer = 1001;
		for (int x = 1; x <= 1000; ++x)
		{
			int bonus = 0;
			for (int i = 0; i < n; ++i)
			{
				if (a[i] % x == 0)
					bonus += (a[i] / x) - 1;
				else
					bonus += (a[i] / x);

			}
			if (bonus + x < answer)
				answer = bonus + x;
		}
		out << "Case #" << t << ": " << answer << endl;
	}
}