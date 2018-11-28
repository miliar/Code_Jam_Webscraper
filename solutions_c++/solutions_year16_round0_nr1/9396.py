#include <iostream>
#include <set>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		int n;
		cin >> n;

		set<int> s;
		long long sum = 0;
		while (s.size() < 10)
		{
			sum += n;
			if (sum == 0)
				break;

			long long sumCopy = sum;
			while (sumCopy)
			{
				s.insert(sumCopy % 10);
				sumCopy /= 10;
			}
		}

		cout << "Case #" << i << ": ";
		if (s.size() < 10)
			cout << "INSOMNIA" << endl;
		else
			cout << sum << endl;
	}
}