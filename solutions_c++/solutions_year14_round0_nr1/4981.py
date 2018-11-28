#include<iostream>
#include<stdio.h>
#pragma warning(disable:4996)
using namespace std;
int main()
{
	//freopen("fun.in", "r", stdin);
	freopen("fun.out", "w", stdout);
	int t, y,i, j, k, line,flag;
	int a[20],b[5],c[5];
	
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		flag = 0;
		cin >> line;
		for (j = 0; j < 16; j++)
		{
			cin >> a[j];
		}
		for (j = 0; j < 4; j++)
		{
			b[j] = a[j + (line - 1) * 4];
		}
		cin >> line;
		for (j = 0; j < 16; j++)
		{
			cin >> a[j];
		}
		for (j = 0; j < 4; j++)
		{
			c[j] = a[j + (line - 1) * 4];
		}
		for (j = 0; j < 4;j++)
		for (k = 0; k < 4; k++)
		{
			if (b[j] == c[k])
			{
				y = b[j];
				flag++;
			}
		}
		if (flag == 1)
			cout << "Case #" << i  << ": " << y << endl;
		else if (flag > 1)
			cout << "Case #" << i << ": Bad magician!" << endl;
		else
			cout << "Case #" << i  << ": Volunteer cheated!"<<endl;

	}
	

	return 0;
}