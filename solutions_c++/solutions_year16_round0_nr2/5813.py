#include <iostream>
#include <string>
#include <stack>
using namespace std;

#define FOR(i, s, n) for(unsigned long long i = (s); i < (n); i++)

bool IsEnd(stack<char> cakes)
{
	while (cakes.size() > 0)
	{
		if (cakes.top() == '-')
		{
			return false;
		}
		cakes.pop();
	}
	return true;
}

void Reverse(stack<char> &cakes, char side, char change)
{
	int count = 0;
	while (cakes.size() > 0 && cakes.top() == side)
	{
		count++;
		cakes.pop();
	}

	for (int i = 0; i < count; i++)
	{
		cakes.push(change);
	}
}

void main()
{
	int T;
	cin >> T;
	FOR(cases, 1, T + 1)
	{
		string str;
		cin >> str;
		stack<char> cakes;

		for (int i = str.size() - 1; i >= 0; i--)
		{
			cakes.push(str[i]);
		}		

		int step = 0;		
		for (;; step++)
		{
			if (IsEnd(cakes))
				break;
			else if (cakes.top() == '+')
				Reverse(cakes, '+', '-');
			else
				Reverse(cakes, '-', '+');
		}

		cout << "Case #" << cases << ": " << step << endl;
	}
}