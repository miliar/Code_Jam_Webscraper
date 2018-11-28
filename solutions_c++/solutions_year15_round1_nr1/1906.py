#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int iCase = 1; iCase <= numCases; iCase++)
	{
		int N = 0;
		cin >> N;

		int x = 0;
		int y = 0;

		vector<int> m;

		for (int i = 0; i < N; i++)
		{
			m.emplace_back();
			cin >> m.back();
		}

		int mprev = m.front();
		int maxEat = 0;

		for (int i = 1; i < N; i++)
		{
			int ate = mprev - m[i];
			y += std::max(ate, 0);
			maxEat = std::max(maxEat, ate);
			mprev = m[i];
		}

		for (int i = 0; i < N-1; i++)
		{
			x += std::min(maxEat, m[i]);
		}


		cout<<"Case #" << iCase << ": " << y << " " << x << endl;
	}

	return 0;
}