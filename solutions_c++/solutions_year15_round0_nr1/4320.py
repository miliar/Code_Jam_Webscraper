#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	int cases;
	int temp;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in >> cases;
	int *sizes = new int[cases];
	int **ptr = new int*[cases];
	string *s = new string[cases];
	for (int i = 0; i < cases; i++)
	{
		in >> sizes[i];
		sizes[i] = sizes[i] + 1;
		ptr[i] = new int[sizes[i]+1];
		in >> s[i];
	}
	for (int i = 0; i < cases; i++)
	{
		for (int j = 0; j < sizes[i]; j++)
		{
			ptr[i][j] = s[i][j]-48;
		}
	}
	int persons = 0;
	int sum = 0;
	for (int j = 0; j < cases; j++)
	{
		persons = 0;
		sum = ptr[j][0];
		for (int i = 0; i < sizes[j]; i++)
		{
			while (sum < i)
			{
				persons++;
				sum++;
			}
			if (i != 0)
				sum = sum + ptr[j][i];
		}
		out <<"Case #"<<j+1 <<": "<< persons << endl;
	}
}