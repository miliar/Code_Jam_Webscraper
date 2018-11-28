#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int cases = 0;
	in >> cases;
	int *rows = new int[cases];
	int *col = new int[cases];
	int *x = new int[cases];
	for (int i = 0; i < cases; i++)
	{
		in >> x[i];
		in >> rows[i];
		in >> col[i];
	}
	bool gab;
	for (int i = 0; i < cases; i++)
	{
		if (x[i]>rows[i] && x[i]> col[i])
		{
			gab = false;
		}
		else if ((rows[i] * col[i]) % x[i] != 0)
		{
			gab = false;
		}
		else if (x[i] == 1)
		{
			gab = true;
		}
		else if (x[i] == 2)
		{
			gab = true;
		}
		else if (x[i] == 3)
		{
			if (rows[i] == 1 || col[i] == 1)
			{
				gab = false;
			}
			else
			{
				gab = true;
			}
		}
		else if (x[i] == 4)
		{
			if (rows[i] < 3 || col[i] < 3)
			{
				gab = false;
			}
			else
			{
				gab = true;
			}
		}
		out << "Case #" << i+1 << ": ";
		if (gab == true)
		{
			out << "GABRIEL" << endl;
		}
		else
		{
			out << "RICHARD" << endl;
		}
	}
}