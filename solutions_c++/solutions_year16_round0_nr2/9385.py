#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
using namespace std;
void inverse(int index, int c, char array[]);
bool check(int limit, char array[]);

void main() {
	ifstream fin("B-small-attempt1.in");
	ofstream fout("output.txt");
	ifstream infile;
	infile.open("B-small-attempt1.in");
	char array[100];
	int n, c, roll, indexer;
	fin >> n;
	string s;
	getline(infile, s);
	for (int i = 1; i <= n; i++)
	{
		getline(infile, s);
		roll = 0;
		c = s.length();
		cout << s;
		cout << c;
		indexer = c - 1;

		for (int y = 0; y < c; y++)
			array[y] = s[y];

		for (int j = 0; j <= c; j++)
		{
			if (check(c, array)) {
				fout << "case #" << i << ":" << " " << roll << endl;
				break;
			}
			else
			{
				if (array[indexer] == '-')
				{
					inverse(indexer, c, array);
					roll++;
				}
				indexer--;
			}
		}
	}

	cin.get();
}
void inverse(int index, int c, char array[])
{
	for (int i = index; i >= 0; i--)
	{
		if (array[i] == '-')
		{
			array[i] = '+';
		}
		else
		{
			array[i] = '-';
		}
	}
}


bool check(int limit, char array[]) {
	for (int i = 0; i < limit; i++)
		if (array[i] == '-')
			return false;
	return true;
}


