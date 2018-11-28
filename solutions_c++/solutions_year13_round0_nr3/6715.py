#include <iostream>
#include <stdio.h>
using namespace::std;

bool isPalindrome(int x)
{
	int y = 0;
	int tmp = x;
	while (tmp)
	{
		y = y * 10 + (tmp % 10);
		tmp /= 10;
	}

	if (x == y)
		return true;
	else
		return false;
}

main ()
{
	int t;
	scanf("%d", &t);

	bool array[1001];
	for (int i = 0; i < 1001; ++i)
		array[i] = false;

	for (int i = 0; i < 33; ++i)
	{
		if (isPalindrome(i * i))
			if (isPalindrome(i))
				array[i * i] = true;
	}
	for (int i = 0; i < t; ++i)
	{
		int a, b;
		scanf("%d", &a);
		scanf("%d", &b);

		int count = 0;
		for (int j = a; j <= b; ++j)
			if (array[j])
				count++;
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
}
