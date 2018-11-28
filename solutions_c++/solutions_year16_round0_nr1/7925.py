#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>

using namespace std;

void addToSet(int cur, set <int>* curSet)
{
	while (cur > 0)
	{
		int i = cur % 10;
		curSet->insert(i);
		cur /= 10;
	}
}

bool checkSet(set <int>* curSet)
{
	for (int i = 0; i <= 9; i++)
		if (curSet->find(i) == curSet->end()) return false;
	return true;
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	set <int> digits;
	int n, k = 1;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		digits.clear();
		int x, k = 1;
		cin >> x;
		if (x == 0)
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		while (true)
		{
			int y = k * x;
			addToSet(y, &digits);
			k++;
			if (checkSet(&digits))
			{
				cout << "Case #" << i << ": " << y << endl;
				break;
			}
		}
	}
	return 0;
}