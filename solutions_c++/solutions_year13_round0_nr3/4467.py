#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

bool palindrome(int value)
{
	stack<int> a;
	queue<int> b;
	int c;

	while(value)
		c = value % 10, value /= 10, a.push(c), b.push(c);

	while(b.size())
	{
		if(a.top() != b.front())
			return false;
		a.pop(), b.pop();
	}

	return true;
}

int main()
{
	int t;
	cin >> t;

	for(int s = 0; s < t; s++)
	{
		int a, b, count = 0;
		cin >> a >> b;
		for(int i = sqrt((double)a); i <= sqrt((double)b); i++)
			if(i * i >= a && i * i <= b)
				if(palindrome(i) && palindrome(i * i))
					count++;
		printf("Case #%d: %d\n", s + 1, count);
	}

	return 0;
}