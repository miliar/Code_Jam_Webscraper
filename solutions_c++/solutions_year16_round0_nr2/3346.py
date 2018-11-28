#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

class Pancake {

private:
	int N;
	bool *data;

public:
	Pancake(string pancakes)
	{
		N = pancakes.size();
		data = new bool[N];

		for (int i = 0; i < N; i++)
		{
			(pancakes[i] == '+') ? data[i] = true : data[i] = false;
		}
	}

	bool first() { return data[0]; }

	bool check()
	{
		for (int i = 0; i < N; i++)
		{
			if (data[i] == false)
				return false;
		}
		
		return true;
	}

	int longestBlank()
	{
		for (int i = N; i > 0; i--)
		{
			if (data[i-1] == false)
				return i;
		}

		return 0;
	}

	int shortestHappy()
	{
		for (int i = 0; i < N; i++)
		{
			if (data[i] && !data[i+1])
				return i + 1;
		}
	}

	void flip(int i)
	{
		bool tmp;

		for (int k = 0; k < (i+1)/2; k++)
		{
			tmp = data[k];
			data[k] = !data[i - k - 1];
			data[i - k - 1] = !tmp;
		}

		//if (i % 2 == 1) data[(i - 1) / 2] = !data[(i - 1) / 2];
	}
};

int main()
{
	int T, ans;
	string cake;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cin >> cake;
		Pancake pancake = Pancake(cake);

		for (ans = 0; ; ans++)
		{
			if (pancake.check()) break;

			else if (pancake.first())
				pancake.flip(pancake.shortestHappy());

			else
				pancake.flip(pancake.longestBlank());
		}

		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}

#endif