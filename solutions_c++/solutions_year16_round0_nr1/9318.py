#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
int sheep(int, int);
int validate(int, int);
int loop(int[]);
void main()
{
	ifstream fin;
	fin.open("A-large.in");
	int T, N, i = 1;
	fin >> T;
	if (validate(T,100) == 1)
	{
		while (i <= T)
		{
			fin >> N;
			if (validate(N, 1000000) == 1)
				sheep(i, N);
			i++;
		}
	}
}
int sheep(int T, int N)
{
	ofstream fout;
	fout.open("output.in", ios::out | ios::app);
	int no = N, i = 1, r, q;
	int check[10] = { 0 };
	if (N == 0)
	{
		fout << "Case #" << T << ": INSOMNIA\n";
		return 0;
	}
	else
	{
		q = no;
		while (loop(check) == 0)
		{
			r = 0;
			if (q > 0)
			{
				r = q % 10;
				q /= 10;
				if (r <= 9 && check[r] == 0)
				{
					check[r] = true;
					if (loop(check) == 1)
						break;
				}
				if (q == 0)
				{
					i++;
					no = N * (i);
					q = no;
				}
			}
		}
		no = N * (i);
		fout << "Case #" << T << ":   " << no << endl;
	}
	return 0;
}
int validate(int T,int a)
{
	if (T >= 0 && T < a+1)
		return 1;
	else
	return 0;
}
int loop(int a[])
{
	for (int i = 0;i < 10;i++)
	{
		if (a[i] == 1)
			continue;
		else
			return 0;
	}
	return 1;
}