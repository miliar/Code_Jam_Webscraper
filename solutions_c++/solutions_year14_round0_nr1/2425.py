#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
	bool count[20];
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		memset(count, 0, sizeof(count));
		for (int x = 1; x <= 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				int data;
				cin >> data;
				if (x == n)
					count[data] = true;
			}
		}
		cin >> n;
		int ans = 0;
		int key = 0;
		for (int x = 1; x <= 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				int data;
				cin >> data;
				if (x == n && count[data])
				{
					key = data;
					ans++;
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (ans == 1)
			cout << key;
		else if (ans == 0)
			cout << "Volunteer cheated!";
		else if (ans > 1)
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}