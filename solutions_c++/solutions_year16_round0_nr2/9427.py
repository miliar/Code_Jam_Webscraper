#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
int happy_up(char[], int, int);
int validate(int, int);
void main()
{
	fstream fin;
	fin.open("B-large.in");
	int T, i = 1, j = 0;
	char S[101] = {NULL};
	fin >> T;
	if (validate(T, 100) == 1)
	{
		while (i <= T)
		{
			j = 0;
			fin >> S;
			while (S[j] != '\0')
			{
				j++;
			}
			happy_up(S, j, i);
			i++;
		}
	}
}
int happy_up(char S[], int i, int T)
{
	ofstream fout;
	fout.open("output.in", ios::out | ios::app);
	int j = i, k = 0;
	while (i >= 0)
	{
		j = i;
		if (S[i] == '-')
		{
			while (j >= 0)
			{
				if (S[j] == '-')
				{
					S[j] = '+';
				}
				else
				{
					S[j] = '-';
				}
				j--;
			}
			k++;
		}
		i--;
	}
	fout << "Case #" << T << ":   " << k << endl;
	return 0;
}
int validate(int T, int a)
{
	if (T >= 0 && T < a + 1)
		return 1;
	else
		return 0;
}