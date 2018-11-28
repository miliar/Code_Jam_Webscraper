#include <iostream>
#include <string>
#include <conio.h>
using namespace std;

int main()
{
	int count;
	int N;
	cin >> count;
	for (int j = 1; j <= count; j++)
	{
		int digit[10] = { 0, };
		int i = 1; int c = 0; int k = 0;
		cin >> N;
		if (N == 0)
		{
			cout << "Case #" << j << ": INSOMNIA" << endl;
			continue;
		}
		
		while (1)
		{
			string number;
			number = to_string(N*i);
			
			for (int test = 0; test < number.length(); test++)
			{
				if (digit[stoi(number.substr(test, 1))] == 0)
					digit[stoi(number.substr(test, 1))] = 1;
			}

			for (int h = 0; h < 10; h++)
			{
				
				if (digit[h] == 1)
				{
					c++;
					digit[h] = 2;
				}
				if (c == 10)
					break;
			}
			
			if (c == 10)
			{
				cout << "Case #" << j << ": " << N*i << endl;
				break;
			}
			i++;
		}
	}
}