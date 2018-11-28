#include<iostream>
#include <string>
#include<vector>
using namespace std;
int main()
{
	int nTests = 0;
	cin >> nTests;
	int n = 0;
	string stack;
	int nFlip = 0;
	for (int i = 1; i <= nTests; i++)
	{
		cin >> stack;
		bool correct = false;
		int j = 0;
		nFlip = 0;
		while (!correct)
		{
			if (stack[0] == '+')
			{
				int k = 0;
				while ((stack[k] == '+') && (k < stack.length()))
				{
					k++;
				}
				if (k != stack.length())
				{
					nFlip++;
					for (int l = 0; l < k; l++)
					{
						stack[l] = '-';
					}
				}
				else{
					correct = true;
				}
			}
			if (stack[0] == '-')
			{
				int k = 0;
				while ((stack[k] == '-') && (k < stack.length()))
				{
					k++;
				}
				if (k != stack.length())
				{
					nFlip++;
					for (int l = 0; l < k; l++)
					{
						stack[l] = '+';
					}
				}
				else
				{
					nFlip++;
					for (int l = 0; l < k; l++)
					{
						stack[l] = '+';
					}
					correct = true;
				}
			}
		}
		cout << "Case #"<<i<<": "<<nFlip << endl;
	}
	//system("pause");
}