#include <iostream>
#include <set>
using namespace std;

long long findNumber(int N)
{
	int i = 1;
	set<int> ans;

	while (true)
	{
		int NN = i * N;
		while (NN)
		{
			ans.insert(NN % 10);
			NN /= 10;
		}

		if (ans.size() == 10)
		{
			break;
		}

		i++;
	}

	return i * N;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;
		if (N == 0)
		{
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else
		{
			cout << "Case #" << t << ": " << findNumber(N) << endl;
		}
	}
	return 0;
}