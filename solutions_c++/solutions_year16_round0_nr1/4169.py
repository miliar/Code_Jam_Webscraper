#include <iostream>
#include <vector>

using namespace std;

int lastNumberSeen(int kase, int N)
{
	if (N == 0)
		return -1;
	vector<int> seen(10, 0);
	int digitsSeen = 0;
	for (int current=N; true; current+=N)
	{
		int val = current;
		while (val)
		{
			if (!seen[val%10])
			{
				seen[val%10] = 1;
				digitsSeen++;
			}
			val /= 10;
		}
		if (digitsSeen== 10)
			return current;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		int N;
		cin >> N;
		int last = lastNumberSeen(t, N);
		cout << "Case #" << t << ": ";
		if (last > 0)
			cout << last;
		else
			cout << "INSOMNIA";
		cout << endl;

	}
	return 0;
}
