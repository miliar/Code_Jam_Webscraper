#include <iostream>
#include <string>

using namespace std;

#define		i	3
#define		j	5
#define		k	7

int multiply(int x, int y)
{
	if (x == 1)
	{
		return y;
	}

	if (x == -1)
	{
		return -y;
	}

	if (y == 1)
	{
		return x;
	}

	if (y == -1)
	{
		return -x;
	}

	int sign = 1;
	if (x < 0)
	{
		x *= (-1);
		sign *= (-1);
	}
	if (y < 0)
	{
		y *= (-1);
		sign *= (-1);
	}

	if (x == i)
	{
		if (y == i)
		{
			return -1 * sign;
		}
		if (y == j)
		{
			return k* sign;
		}
		if (y == k)
		{
			return -j* sign;
		}
	}

	if (x == j)
	{
		if (y == i)
		{
			return -k* sign;
		}
		if (y == j)
		{
			return -1 * sign;
		}
		if (y == k)
		{
			return i* sign;
		}
	}

	if (x == k)
	{
		if (y == i)
		{
			return j* sign;
		}
		if (y == j)
		{
			return -i* sign;
		}
		if (y == k)
		{
			return -1 * sign;
		}
	}

	return 0xC7A54;
}

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int L, X;
		string letters;
		cin >> L >> X >> letters;

		int current_result = 1;
		int last_letter_reached = 0;
		for (int times = 0; times < X; times++)
		{
			for (int index = 0; index < L; index++)
			{
				char operand = letters[index];
				int op = 2 * (operand - 'i' + 1) + 1;
				current_result = multiply(current_result, op);

				if (current_result == i && last_letter_reached == 0)
				{
					last_letter_reached = i;
					current_result = 1;
				}
				else if (current_result == j && last_letter_reached == i)
				{
					last_letter_reached = j;
					current_result = 1;
				}
				else if (current_result == k && last_letter_reached == j)
				{
					last_letter_reached = k;
					current_result = 1;
				}
			}
		}

		if (current_result == 1 && last_letter_reached == k)
		{
			cout << "Case #" << t + 1 << ": " << "YES" << '\n';
		}
		else
		{
			cout << "Case #" << t + 1 << ": " << "NO" << '\n';
		}
	}

	return 0;
}