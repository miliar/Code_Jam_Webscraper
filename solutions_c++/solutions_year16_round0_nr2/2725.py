#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

bool digits[10];

void findDigits(int n)
{
	if (n < 10)
	{
		digits[n] = true;
		return;
	}
	digits[n%10] = true;
	findDigits(n / 10);
}

bool isDone()
{
	for (int i = 0; i < 10; ++i)
	{
		if (!digits[i]) return false;
	}
	return true;
}

void clear()
{
	for (int i = 0; i < 10; ++i)
	{
		digits[i] = false;
	}
}

int main_q1() {
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; ++tc)
	{
		int n, m;
		cin >> n;
		m = n;
		clear();
		if (m > 0)
		{
			findDigits(m);
			while (!isDone())
			{
				m += n;
				findDigits(m);
			}
			cout << "Case #" << tc << ": " << m << endl;
		}
		else
		{
			cout << "Case #" << tc << ": INSOMNIA" << endl;
		}
	}

	return 0;
}

int main()
{
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; ++tc)
	{
		string s;
		cin >> s;
		int result = s[0] == '-' ? 1 : 0;
		for (int i = s.find('+'); i != string::npos; i = s.find('+',i))
		{
			i = s.find('-', i);
			if (i != string::npos)
			{
				result += 2;
			}
		}
		cout << "Case #" << tc << ": " << result << endl;
	}

	return 0;
}