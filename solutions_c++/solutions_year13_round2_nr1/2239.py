// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int c = 0; c < numCases; ++c) 
	{
		unsigned long a, n;
		cin >> a >> n;
		vector<unsigned long> m(n);

		unsigned long i = 0;
		for (; i < n; ++i)
			cin >> m[i];

		sort(m.begin(), m.end());

		unsigned long N = 0;
		i = 0;
		while (i < m.size() && N < m.size() - i)
		{
			for (; i < m.size() && m[i] < a; ++i)
				a += m[i];
			if (i < m.size()) {
				unsigned long t = 0;
				for (; a <= m[i] && t < m.size() - i; a += (a - 1), ++t);
				if (t < m.size() - i)
					N += t;
				else
					N += m.size() - i;
			}
		}

		cout << "Case #" << c+1 << ": " << N << endl;
	}
		
	return 0;
}
