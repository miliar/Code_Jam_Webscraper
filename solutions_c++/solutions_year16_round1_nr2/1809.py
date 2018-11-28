#include <iostream>
#include <math.h>
#include <fstream> 

using namespace std;

int main()
{
	ifstream f;
	f.open("1.in");
	ofstream f1;
	f1.open("2.txt");
	int T, n, x, y, temp=0;
	int mas[100000];
	f >> T;
	for (int i = 0; i < T; i++)
	{
		for (int k = 0; k < 100000; k++)
		{
			mas[k] = 0;
		}
		f >> n;
		int *arr = new int [n];
		for (int j = 0; j <(2*n-1)*n ; j++)
		{
			f >> x;
			mas[x - 1]++;
		}
		y = 0;
		f1 << "Case #" << i+1 << ": ";
		while (temp<n)
		{
			if (mas[y] % 2 == 1)
			{
				temp++;
				f1 << y + 1 << " ";
			}
			y++;
		}
		temp = 0;
		f1 << endl;
	}
	system("pause");
}