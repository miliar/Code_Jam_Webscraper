#include<iostream>
#include<cstring>
using namespace std;

char str[100][101];
int itr[100];

int main()
{
	int nCase;
	cin >> nCase;
	for (int z = 1; z <= nCase; ++z)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> str[i];
		bool success = true;
		int a, b, c;
		int l0, l1;
		l0 = strlen(str[0]);
		l1 = strlen(str[1]);
		a = b = c = 0;
		while (success && a < l0 && b < l1)
		{
			if (str[0][a] == str[1][b])
			{
				++a;
				++b;
			}
			else{
				if (str[0][a] == str[0][a - 1])
				{
					++a;
					++c;
				}
				else if (str[1][b] == str[1][b - 1])
				{
					++b;
					++c;
				}else
					success = false;
			}
		}
		while (success && a < l0)
		{
			if (str[0][a] == str[1][b - 1])
			{
				++a;
				++c;
			}else
				success = false;
		}
		while (success && b < l1)
		{
			if (str[1][b] == str[0][a - 1])
			{
				++b;
				++c;
			}else
				success = false;
		}
		//bool success = true;
		//bool allSame;
		//char tar;
		//memset(itr, 0, sizeof(itr));
		//while (success)
		//{
		//	allSame = true;
		//	tar = str[0][itr[0]];
		//	for (int i = 1; i < n && success; ++i)
		//	{
		//		if (str[i][itr[i]] != tar)
		//			allSame = false;
		//	}
		//	if (allSame)
		//		for (int i = 0; i < n; ++i)
		//			++itr[i];
		//	else
		//	{

		//	}
		//}
		cout << "Case #" << z << ": ";
		if (!success)
			cout << "Fegla Won" << endl;
		else
			cout << c << endl;
	}
	return 0;
}