#include <iostream>
#include <string>


using namespace std;

#include <iostream>
#include <string>
using namespace std;

int GetLastPlus(string arr, int lastplus)
{
	while (lastplus >= 0 && arr[lastplus] == '+')
	{
		lastplus--;
	}
	return lastplus;
}


void flip(string* arr, int i)
{
	if ((*arr)[i] == '+')
		(*arr)[i] = '-';
	else
		(*arr)[i] = '+';
}

void swap(string* arr, int x, int y)
{
	char c = (*arr)[x];
	(*arr)[x] = (*arr)[y];
	(*arr)[y] = c;
}

void flipAndSwap(string* arr, int x, int y)
{
	char temp;
	while (x<y)
	{
		flip(arr, x);
		flip(arr, y);
		swap(arr, x, y);
		x++;
		y--;
	}
	if (y == x)
		flip(arr, x);
}


int main() {
	// your code goes here
	string s;

	int t, lastplus;

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int count = 0;
		int k = 0;
		cin >> s;
		int l = s.length() - 1;
		lastplus = GetLastPlus(s, l);
		if (lastplus == -1)
		{
			cout << "Case #" << i << ": 0\n";
			continue;
		}

		while (lastplus != -1)
		{
			if (s[k] == '+')
			{
				while (k <= lastplus&&s[k] == '+')
				{
					s[k] = '-';

					k++;
				}
				count++;
			}
			flipAndSwap(&s, 0, lastplus);
			count++;
			k = 0;
			lastplus = GetLastPlus(s, lastplus);

		}
		cout << "Case #" << i << ": " << count << "\n";
		count = 0;
		s.clear();
	}
}


