#include <iostream>
using namespace std;

typedef long long ll;

class Tracker
{
public:
	Tracker() : setCount(10)
	{
		memset(arr, 0, 10 * sizeof(int));
	}


	void init(ll n)
	{
		//arr[0] = 1; setCount--;
		updateTracker(n);
	}
	void updateTracker(ll n)
	{
		while (n)
		{
			int dig = n % 10;
			if (0 == arr[dig])
			{
				arr[dig] = 1;
				setCount--;
			}
			n = n / 10;
		}
	}

	int arr[10];
	int setCount;
};

int main(void)
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T = 0;
	cin >> T;
	ll Answer = 0;
	int N; 

	for (int i = 0; i < T; ++i)
	{
		cin >> N;
		if (N > 0)
		{
			Tracker t;
			t.init(N);
			for (int j = 2; ; ++j)
			{
				t.updateTracker(j*N);
				if (t.setCount == 0)
				{
					Answer = j*N;
					break;
				}
			}
		}
		else
		{
			Answer = -1;
		}

		if (Answer == -1)
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << i + 1 << ": " << Answer << endl;
	}
	return 0;
}
