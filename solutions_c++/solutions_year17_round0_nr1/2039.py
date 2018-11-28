#include <iostream>
#include <cstring>
using namespace std;

void flip(char& c)
{
	switch(c)
	{
		case '+': c = '-';
		          break;
		case '-': c = '+';
		          break;
		default : cout << "Invalid";
	}
}

int main() {
	int t, k, count, j;
	char s[1000];
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> s >> k;
		count = 0;
		int length = strlen(s) + 1 - k;
		for(j = 0; j < length; j++)
		{
			if(s[j] == '-')
			{
				for(int m = 0; m < k; m++)
					flip(s[j + m]);
				count++;
			}
		}
		length = strlen(s);
		for(; j < length; j++)
		{
			if(s[j] == '-')
				break;
		}
		cout << "Case #" << i + 1 << ": ";
		if(j == length)
			cout << count << "\n";
		else
			cout << "IMPOSSIBLE" << "\n";
	}
	return 0;
}
