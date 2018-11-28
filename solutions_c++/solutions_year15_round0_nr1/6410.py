#include<iostream>

using namespace std;

void solveCase()
{
	int ms;
	unsigned char tmp;
	unsigned char sl[2000];
	cin >> ms;
	for (int i = 0; i <= ms; i++)
	{
		cin >> tmp;
		sl[i] = tmp - 48;
	}

	int standing = 0;
	int friends = 0;

	for (int i = 0; i <= ms; i++)
	{
		if (i > standing)
		{
			friends += i - standing;
			standing = i;
		}
		standing += sl[i];
	}

	cout << friends;
}

int main()
{
	int cases;
	cin >> cases;
	for (int c = 0; c < cases; c++)
	{
		cout << "Case #" << c + 1 << ": ";
		solveCase();
		cout << endl;
	}
}
