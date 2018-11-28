#include <iostream>

using namespace std;

int t;
string str;

void reverse(int from, int to)
{
	int i = from, j = to;
	while (i <= j)
	{
		char ch = str[i];
		str[i] = str[j];
		str[j] = ch;
		i++;
		j--;
	}
}

bool valid()
{
	for (int i = 0; i < str.length(); ++i)
	{
		if (str[i] == '-')
			return false;
	}

	return true;
}

int solve()
{
	int front = 0, rear = str.length() - 1;
	int cnt = 0;
	while (!valid())
	{
		while (str[rear] == '+')
			rear--;

		if (str[front] == '-')
		{
			reverse(front, rear);

			for (int i = front; i <= rear; ++i)
				str[i] = ((str[i] == '-') ? '+' : '-');

			cnt++;
		}
		else
		{
			int i = 0;
			while (str[front + i] == '+')
			{
				str[front + i] = '-';
				i++;
			}
			cnt++;
		}
	}

	return cnt;
}

void getInput()
{
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> str;

		printf("Case #%d: %d\n", i, solve());
	}
}

int main(int argc, char const *argv[])
{
	getInput();
	return 0;
}